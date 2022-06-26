# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import datetime


def main(VERBOSE: bool = False):
    MAX_FILE_DATE = "01-06-2022"
    FILES_DIRECTORY = os.path.join(os.getcwd(), "static", "hold")
    #
    print("[MAIN] version all changed static files in the PWA project \n")

    # list all files in directory recursively
    file_list = list_all_files_in_directory(FILES_DIRECTORY)

    # print files list
    if VERBOSE: print_files_in_list(file_list)

    # version all changed static files in the directory
    version_changed_files(file_list, MAX_FILE_DATE)

    print("\n[MAIN] versioning finished")


def list_all_files_in_directory(directory: str) -> list:
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_info_dict = {}
            file_info_dict["file_path"] = os.path.join(root, file)
            file_info_dict["file_name"] = file
            file_info_dict["file_extension"] = os.path.splitext(file)[1]
            file_info_dict["file_size"] = os.path.getsize(file_info_dict["file_path"])
            file_info_dict["file_modified_time"] = os.path.getmtime(file_info_dict["file_path"])
            if "-" in file:
                file_info_dict["file_version"] = file.split("-")[1].strip(file_info_dict["file_extension"])
            else:
                file_info_dict["file_version"] = ""

            files_list.append(file_info_dict)
    return files_list


def version_changed_files(files_list: list, version_files_after_data: str) -> None:
    """
    version all changed static files in the directory
    :param files_list:
    :param version_files_after_data: date in format DD-MM-YYYY
    :return: nothing
    """
    max_file_age_epoch = convert_date_to_epoch_timestamp(version_files_after_data)
    # print(max_file_age_epoch)
    for file in files_list:
        if file["file_modified_time"] > max_file_age_epoch:
            # print(file["file_path"])
            if file["file_version"] != "" and file["file_extension"] in [".js", ".css", ".html"]:
                print("[INFO] file to be versioned: " + file["file_path"])
                new_file_version = datetime.datetime.now().strftime("%d%b%Y")
                new_file_name = file["file_name"].split("-")[0] + "-" + new_file_version + file["file_extension"]
                print("[-->] new file name: ", new_file_name)
                os.rename(file["file_path"], file["file_path"].replace(file["file_version"], new_file_version))


def convert_date_to_epoch_timestamp(date_str: str) -> int:
    """
    convert date to epoch timestamp
    :param date_str: date in format DD-MM-YYYY
    :return: epoch timestamp
    """
    date_list = date_str.split("-")
    input_date_epoch = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0])).timestamp()
    first_epoch = datetime.datetime(1970, 1, 1).timestamp()
    return int(input_date_epoch - first_epoch)


def print_files_in_list(files_list: list):
    print("\nFiles list:")
    for file in files_list:
        print(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    VERBOSE = False
    main(VERBOSE)
