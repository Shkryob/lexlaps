from __future__ import print_function
from time import sleep

import logging
import os
import subprocess
import sys

import gphoto2 as gp

def take_a_photo(id, tries=1):
    try:
        logging.basicConfig(
            format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        gp.check_result(gp.use_python_logging())
        camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(camera))
        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(
            camera, gp.GP_CAPTURE_IMAGE))
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join('/home/ubuntu/lexlaps/tmp', str(id) + '_' + file_path.name)
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(
            camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        gp.check_result(gp.gp_file_save(camera_file, target))
        gp.check_result(gp.gp_camera_exit(camera))
    except:
        if tries < 4:
            take_a_photo(id, tries + 1)

def main():
    for i in range(0, 1800):
        take_a_photo(i)
        sleep(30)
    return 0

if __name__ == "__main__":
    sys.exit(main())