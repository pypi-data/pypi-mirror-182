import glob
import os
import re
from datetime import date, datetime, timedelta
from typing import List, Literal, Optional


def get_folders(
    folders: List[str] | str, area: Literal["MP", "G2", "G3", "O2"]
) -> List[str]:
    folders_list = []
    result = []
    if isinstance(folders, str):
        folders_list = folders.split(",")
    else:
        folders_list = folders
    for folder in folders_list:
        if area in folder:
            result.append(folder)
    return result


def get_pass_files(
    self,
    folders: List[str],
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
) -> List[str]:

    result = []
    for folder in folders:
        folder = self.root_dir + folder
        if (start_date and not end_date) or (end_date and not start_date):
            date = start_date if start_date else end_date
            if date:
                files = glob.glob(
                    r"*%s.txt" % (date.isoformat()),
                    root_dir=folder,
                )
            else:
                files = []
            if files:
                for file in files:
                    result.append(os.path.join(folder, file))

        elif start_date and end_date:
            if end_date - start_date < timedelta(days=1):
                files = glob.glob(
                    r"*%s.txt" % (start_date.isoformat()),
                    root_dir=folder,
                )
                if files:
                    for file in files:
                        result.append(os.path.join(folder, file))
            else:
                date = start_date
                while date < end_date:
                    files = glob.glob(
                        r"*%s.txt" % (date.isoformat()),
                        root_dir=folder,
                    )

                    date = date + timedelta(days=1)
                    if files:
                        for file in files:
                            result.append(os.path.join(folder, file))
        else:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    result.append(file_path)

    return result


def get_files(
    root_dir: str,
    folders: List[str] | str,
    system: Literal["pass", "tds", "tvs"],
    start_datetime: Optional[datetime] = None,
    end_datetime: Optional[datetime] = None,
    area: Optional[Literal["G2", "G3", "O2"]] = None,
    tcs_type: Optional[Literal["trace", "slow"]] = None,
) -> List[str]:
    files = []
    files_found = []
    if start_datetime > end_datetime:
        start_datetime, end_datetime = end_datetime, start_datetime
    if system != "pass" and area == "MP":
        raise Exception("Only pass has a MPSS(main patient safety system)!")
    date_delta = end_datetime.date() - start_datetime.date()
    if date_delta.days > 0:
        days = [
            start_datetime.date() + timedelta(days=i) for i in range(date_delta.days)
        ]
    else:
        days = [start_datetime.date()]
    if isinstance(folders, str):
        folders = [folders]
    for day in days:
        for folder in folders:
            files = files + glob.glob(
                os.path.join(
                    folder, f"*{system.lower()}*{datetime.strftime(day, '%Y%m%d')}*"
                )
            )
    if files.count == 1:
        return files
    if not files:
        raise Exception(
            r"No files found! make sure the files are in $root_dir/path {area}/(TcsTrace/SlowControl)/*"
        )
    file_dict = {}
    for i, timestamp in enumerate(re.findall(r"\d{8}-\d{6}", "".join(files))):
        file_dict[datetime.strptime(timestamp, "%Y%m%d-%H%M%S")] = files[i]
    timestamps = list(file_dict.keys())
    closest_start_datetime = 0
    closest_end_datetime = len(timestamps)
    for index, timestamp in enumerate(sorted(timestamps)):
        if timestamp < start_datetime:
            closest_start_datetime = index
        if timestamp > end_datetime:
            closest_end_datetime = index
            break

    timestamps = timestamps[closest_start_datetime:closest_end_datetime]
    for t in timestamps:
        files_found.append(file_dict[t])
    return files_found
