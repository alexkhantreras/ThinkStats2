# This is chap01ex.py. It is included in the downloaded repo and contains the
# skeleton of programming exercises to complete for chapter 1 of ThinkStats2.

################################################################################

# Setting up our environment

from __future__ import print_function
import sys
import numpy as np
import nsfg
import thinkstats2

################################################################################

# A) Write a function that reads the respondent file, 2002FemResp.dat.gz

# This is done with functions from the thinkstats2 module and in a similar way
# to how 2002ReadFemPreg was processed in section 1.3 of the text.

def ReadFemResp(dct_file = '2002FemResp.dct',
                dat_file = '2002FemResp.dat.gz',
                nrows = None):

    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression = 'gzip', nrows = nrows)
    return df

################################################################################

# B) Compare the values of the recode 'pregnum', which indicates how many times
# each respondent has been pregnant, to the results published in the NSFG codebook

# In short, we need to verfiy that the number of pregnancies for each caseid in
# the response dataset (resp) matches the number of rows corresponding to that
# caseid in the pregnancy dataset (preg).

def VerifyPregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True

################################################################################

# This is where we'll test the quality of our functions in this script. We'll run
# a few quality checks confirming number of records, value of a specific record,
# and run the function VerifyPregnum.

def main(script):
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(VerifyPregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

################################################################################
