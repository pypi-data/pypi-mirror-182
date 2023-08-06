# -*- coding: utf-8 -*-
#  Copyright (C) 2021- BOUFFALO LAB (NANJING) CO., LTD.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import re
import os
import sys
import time

try:
    import bflb_path
except ImportError:
    from libs import bflb_path
from libs import bflb_utils

chip_dict = ("bl602","bl702","bl702l","bl606p", "bl808","bl616")

def firmware_post_process(args, chipname="bl60x"):
    sub_module = __import__("libs." + chipname, fromlist=[chipname])
    sub_module.firmware_post_process_do.firmware_post_proc(args)

def run():
    parser = bflb_utils.firmware_post_proc_parser_init()
    args = parser.parse_args()
    # args = parser_image.parse_args("--image=media", "--signer=none")
    bflb_utils.printf("Chipname: %s" % args.chipname)
    if args.chipname in chip_dict: 
        firmware_post_process(args,  args.chipname)
    else:
        bflb_utils.printf("Please set correct chipname config, exit")


if __name__ == '__main__':
    run()
