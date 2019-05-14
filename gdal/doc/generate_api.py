#!/usr/bin/env python

def generate_rst(rst_filename, anchor_name, description, files):

    rst_f = open(rst_filename,"wt")
    rst_f.write(""".. WARNING ! This file is autogenerated by generate_api.py. DO NOT MODIFY IT directly !

.. _%s:

================================================================================
%s
================================================================================

""" % (anchor_name, description))

    for h_file in files:
        rst_f.write("%s\n" % h_file)
        rst_f.write(('-' * len(h_file)) + '\n')
        rst_f.write('\n')
        rst_f.write('.. doxygenfile:: %s\n' % h_file)
        rst_f.write('   :project: api\n')
        rst_f.write('\n')


cpl_files = [
    "cpl_atomic_ops.h",
    "cpl_auto_close.h",
    "cpl_config_extras.h",
    "cpl_config.h",
    "cpl_conv.h",
    "cpl_csv.h",
    "cpl_error.h",
    "cpl_hash_set.h",
    "cpl_http.h",
    "cpl_json.h",
    "cplkeywordparser.h",
    "cpl_list.h",
    "cpl_minixml.h",
    "cpl_minizip_ioapi.h",
    "cpl_minizip_unzip.h",
    "cpl_minizip_zip.h",
    "cpl_multiproc.h",
    "cpl_odbc.h",
    "cpl_port.h",
    "cpl_progress.h",
    "cpl_quad_tree.h",
    "cpl_spawn.h",
    "cpl_string.h",
    "cpl_time.h",
    "cpl_virtualmem.h",
    "cpl_vsi_error.h",
    "cpl_vsi.h",
    "cpl_vsi_virtual.h"
]

generate_rst("source/api/cpl.rst", "cpl", "Common Portability Library", cpl_files)