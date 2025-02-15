import argparse
import banner
import module_image

metadata_images = {}

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process a file and perform operations on its lines.")
    parser.add_argument("-d", "--file", type=str, required=True, help="File containing urls")
    parser.add_argument("-v", "--verbose", action="store_true", help="Shows you everything!")
    return parser.parse_args()

if __name__ == '__main__':
    print(banner.banner)
    args = parse_arguments()
    image_urls = module_image.scrape_images_from_file(args.file)
    for url in image_urls:
        meta_data_capture = module_image.image_meta(url, args.verbose)
        if meta_data_capture != None:
            metadata_images[url] = meta_data_capture

    data = {
        'title': f"MPMetaSpy report.",
        'images': metadata_images,
    }
    report_title = module_image.generate_summary(data)
