# Version_Static_Files
version control static files based on date modified. For use with PWA projects where static files need their name changed to update


## How To Use:
* modify Date and Directory in Main function
* run: `Python3 version_static_files.py`

## What It Does:
* check for static files in directory with naming convention: `something-ddMonYYYY.ext` ex: `something-25Jun2022.css`
* if file modified time is after [MAX_FILE_DATE] in Main function, then name of file is versioned to todays date in same format

## TODO:
* instead of date modified, version all files in changed in current commit

Cheers,
Mark
