import io
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from jinja2 import FileSystemLoader, Environment


def extract_images(url):
    try:
        response = requests.get(url, timeout=10)  # Fetch page content
        response.raise_for_status()  # Raise error for bad responses
    except requests.RequestException as e:
        print(f"[Error] Could not fetch {url}: {e}")
        return []  # Return empty list if error

    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = set()

    # Extract images from <img> tags
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if src.startswith(('http', 'https')):  # Absolute URL
                image_urls.add(src)
            else:
                image_urls.add(requests.compat.urljoin(url, src))  # Convert relative to absolute

    # Extract linked images from <a> tags (href ends with an image extension)
    for link in soup.find_all('a', href=True):
        if link['href'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp')):
            if link['href'].startswith(('http', 'https')):
                image_urls.add(link['href'])
            else:
                image_urls.add(requests.compat.urljoin(url, link['href']))

    return list(image_urls)

def scrape_images_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"[Error] File {file_path} not found.")
        return

    all_images = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            url = line.strip()
            if url:
                print(f"[Info]Scraping images from: {url}")
                images = extract_images(url)
                all_images.update(images)

    return all_images

def image_meta(img_url, verbose):
    metadata = {}
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()
        image_content = io.BytesIO(response.content)
        if image_content != None:
            image = Image.open(image_content)
            metadata['url'] = img_url
            metadata['format'] = image.format
            metadata['size'] = image.size

            exif_data = image._getexif()
            if exif_data:
                exif = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}

                # Camera info
                metadata['camera_info'] = {
                    'Make': exif.get('Make'),
                    'Model': exif.get('Model'),
                }

                # GPS Info
                gps_info = exif.get('GPSInfo')
                if gps_info:
                    def convert_to_degrees(value):
                        d, m, s = value
                        return d[0] / d[1] + (m[0] / m[1]) / 60 + (s[0] / s[1]) / 3600

                    if 2 in gps_info and 4 in gps_info:
                        metadata['location'] = f"{gps_info[1]} {gps_info[2]}, {gps_info[3]}{gps_info[4]}"
                    else:
                        metadata['location'] = exif.get('GPSInfo')
            return metadata
        else:
            return None
    except Exception as e:
        if verbose:
            print(f"[Error] Failed to get metadata for image {img_url}: {e}")
        return None

def convert_to_degrees(value):
    """Convert GPS coordinates from EXIF format to degrees."""
    def rational_to_float(rational):
        return rational[0] / rational[1] if isinstance(rational, tuple) else float(rational)

    d = rational_to_float(value[0])
    m = rational_to_float(value[1])
    s = rational_to_float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def generate_summary(data):

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template/report.html')
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d")
    data['file_name'] = f"reports/{formatted_time}-"
    output = template.render(data)
    with open(f"reports/report{formatted_time}.html", 'w') as f:
        f.write(output)

    return f"reports/report{formatted_time}.html"