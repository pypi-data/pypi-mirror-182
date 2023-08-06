#ifndef __DAAB__CXX__API__
#define __DAAB__CXX__API__

#include <iostream>
#include <fstream>
#include <sstream>

#include <algorithm>
#include <chrono>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstring>

#include <math.h>
#include <memory.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/time.h>

#include <cblas.h>

namespace daab
{
    class DragonAIAlphaBase
    {
    private:
        int nThreads;
        void *db;

    public:
        double **x;
        int *ut;
        DragonAIAlphaBase();
        ~DragonAIAlphaBase();
        void Init(int, int *);
        void ONL2FIELDX(int, int *);
    };
}

#endif
