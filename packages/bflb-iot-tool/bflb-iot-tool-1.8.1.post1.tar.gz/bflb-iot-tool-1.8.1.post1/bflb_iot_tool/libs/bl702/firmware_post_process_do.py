# -*- coding:utf-8 -*-

import os
import sys
import hashlib
import binascii
import codecs

import ecdsa

from CryptoPlus.Cipher import AES as AES_XTS

from libs import bflb_utils
from libs.bflb_utils import img_create_sha256_data, img_create_encrypt_data

def firmware_post_proc_update_flash_crc(image_data):
    flash_cfg_start=8
    crcarray = bflb_utils.get_crc32_bytearray(image_data[flash_cfg_start+4:flash_cfg_start+4+84])
    image_data[flash_cfg_start+4+84:flash_cfg_start+4+84+4] = crcarray
    bflb_utils.printf("Flash config crc: ", binascii.hexlify(crcarray))
    return image_data

def firmware_post_proc_update_clock_crc(image_data):
    clockcfg_start=8+4+84+4
    crcarray = bflb_utils.get_crc32_bytearray(image_data[clockcfg_start+4:clockcfg_start+12])
    image_data[clockcfg_start+12:clockcfg_start+12+4] = crcarray
    bflb_utils.printf("Clock config crc: ", binascii.hexlify(crcarray))
    return image_data

def firmware_post_proc_update_bootheader_crc(image_data):
    crcarray = bflb_utils.get_crc32_bytearray(image_data[0:172])
    image_data[172:172+4] = crcarray
    bflb_utils.printf("Bootheader config crc: ", binascii.hexlify(crcarray))
    return image_data

# get hash ignore ignore
def firmware_post_proc_get_hash_ignore(image_data):
    bootcfg_start=(4+4)+(4+84+4)+(4+8+4)
    return  (image_data[bootcfg_start + 2] >> 1) & 0x1

# get hash ignore ignore
def firmware_post_proc_enable_hash_cfg(image_data):
    bootcfg_start=(4+4)+(4+84+4)+(4+8+4)
    image_data[bootcfg_start + 2]&=(~0x02)
    return  image_data

# get image offset
def firmware_post_proc_get_image_offset(image_data):
    cpucfg_start=(4+4)+(4+84+4)+(4+8+4)+12
    return  ((image_data[cpucfg_start + 0])+
             (image_data[cpucfg_start + 1]<<8) +
             (image_data[cpucfg_start + 2]<<16) +
             (image_data[cpucfg_start + 3]<<24) )

def firmware_post_proc_update_hash(image_data,force_update,args):
    #get image offset
    image_offset=firmware_post_proc_get_image_offset(image_data)
    bflb_utils.printf("Image Offset:"+hex(image_offset))
    #udpate image len
    bootcfg_start=(4+4)+(4+84+4)+(4+8+4)
    image_data[bootcfg_start+4 :bootcfg_start +4+4]=bflb_utils.int_to_4bytearray_l(len(image_data)-image_offset)
    #add apeend data
    if args.hd_append!=None:
        bflb_utils.printf("Append bootheader data")
        bh_append_data=firmware_get_file_data(args.hd_append)
        if len(bh_append_data)<=image_offset-512:
            image_data[image_offset-len(bh_append_data):image_offset]=bh_append_data
        else:
            bflb_utils.printf("Append data is too long,not append!!!!!!",len(bh_append_data))
    #udpate hash
    if firmware_post_proc_get_hash_ignore(image_data) ==1:
        if force_update==False:
            bflb_utils.printf("Image hash ignore,not calculate")
            return image_data
    image_data=firmware_post_proc_enable_hash_cfg(image_data)
    hash = img_create_sha256_data(image_data[image_offset:len(image_data)])
    bflb_utils.printf("Image hash:",binascii.hexlify(hash))
    image_data[bootcfg_start + 16:bootcfg_start + 16+32]=hash

    return image_data

def firmware_get_file_data(file):
    with open(file, 'rb') as fp:
        data = fp.read()
    return bytearray(data)

def firmware_save_file_data(file,data):
    datas = []
    with open(file, 'wb+') as fp:
        fp.write(data)
        fp.close()

def firmware_post_proc(args):
    bflb_utils.printf("========= sp image create =========")

    image_data=firmware_get_file_data(args.imgfile)
    if len(image_data)%16 !=0:
        image_data=image_data+bytearray(16-len(image_data)%16)

    image_data=firmware_post_proc_update_flash_crc(image_data)
    image_data=firmware_post_proc_update_clock_crc(image_data)
    if args.publickey!=None:
        image_data=firmware_post_proc_update_hash(image_data,True,args)
    else:
        image_data=firmware_post_proc_update_hash(image_data,False,args)
    image_data=firmware_post_proc_update_bootheader_crc(image_data)
    firmware_save_file_data(args.imgfile,image_data)


if __name__ == '__main__':
    data_bytearray = codecs.decode(
        '42464E500100000046434647040101036699FF039F00B7E904EF0001C72052D8' +
        '060232000B010B013B01BB006B01EB02EB02025000010001010002010101AB01' +
        '053500000131000038FF20FF77030240770302F02C01B004B0040500FFFF0300' +
        '36C3DD9E5043464704040001010105000101050000010101A612AC8600014465' +
        '0020000000000000503100007A6345494BCABEC7307FD8F8396729EB67DDC8C6' +
        '3B7AD69B797B08564E982A8701000000000000000000000000000000000000D8' +
        '0000000000010000000000000000000000200100000001D80000000000010000' +
        '0000000000000000002002000000025800000000000100000000000000000000' +
        '00200300000003580000000000010000D0C57503C09E75030020040000000458' +
        '0000000000000000000000000000000000000000000000000000000000000000' +
        '0000000000000000000000000000000000000000000000000000000000000000' +
        '00000000000000000000000000000000000000000000000000000000935F92BB', 'hex')
    key_bytearray = codecs.decode(
        'fffefdfcfbfaf9f8f7f6f5f4f3f2f1f0000102030405060708090a0b0c0d0e0f', 'hex')
    #key = (codecs.decode('00112233445566778899AABBCCDDEEFF', 'hex'), codecs.decode('112233445566778899AABBCCDDEEFF00', 'hex'))
    need_reverse_iv_bytearray = codecs.decode('01000000000000000000000000000000', 'hex')
    iv_bytearray = codecs.decode(reverse_iv(need_reverse_iv_bytearray), 'hex')
    #iv_bytearray = codecs.decode('000000000000000000000000000000000', 'hex')
    img_create_encrypt_data_xts(data_bytearray, key_bytearray, iv_bytearray, 0)
