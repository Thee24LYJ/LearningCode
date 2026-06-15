// 参考：https://mp.weixin.qq.com/s/HOQOFlMPjty-h74QWCZ0TA
// 获取UTC时间戳、格式化时间及本地时区
#include <stdio.h>
#include <time.h>

int main(int argc, char **argv)
{
    // 获取UTC时间戳
    time_t utc_time = time(NULL);
    printf("UTC timestamp = %ld s\n", utc_time);

    // 从UTC时间戳计算时间(格式化)
    struct tm gmt_tm;
    gmtime_r(&utc_time, &gmt_tm);
    printf("UTC time = %.4d-%.2d-%.2d %.2d:%.2d:%.2d\n",
            gmt_tm.tm_year + 1900,
            gmt_tm.tm_mon + 1,
            gmt_tm.tm_mday,
            gmt_tm.tm_hour,
            gmt_tm.tm_min,
            gmt_tm.tm_sec);

    // 计算本地时间(格式化)
    struct tm local_tm;
    localtime_r(&utc_time, &local_tm);
    printf("Local time = %.4d-%.2d-%.2d %.2d:%.2d:%.2d\n",
            local_tm.tm_year + 1900,
            local_tm.tm_mon + 1,
            local_tm.tm_mday,
            local_tm.tm_hour,
            local_tm.tm_min,
            local_tm.tm_sec);

    // 计算本地时区
    int tz_offset = local_tm.tm_hour - gmt_tm.tm_hour;
    if (tz_offset < -12)
    {
        tz_offset += 24;
    }
    else if (tz_offset > 12)
    {
        tz_offset -= 24;
    }

    printf("Local timezone = UTC%+d\n", tz_offset);
    return 0;
}
