%% 浮点和定点数转换

% 浮点数转为定点数
float_v = -0.54;
signed_flag = 1;
int_len = 9;
frac_len = 7;
a = fi(float_v,signed_flag,int_len,frac_len);
fix_num = bin(a);
fprintf('%f -> %s\n',float_v,fix_num);

% 定点数转为浮点数(浮点数转换为定点数会损失精度，因此从定点数还原为浮点数不一定和原来的一样)
fix_bin = bin2dec(fix_num); % 二进制数大小
basic_unit = 1/2^frac_len;  % 基本大小
float_fix = fix_bin * basic_unit;   % 得到大致的数据
max_float = 2^(int_len-frac_len);   % 无符号数最大值
if(signed_flag == 1)
    if(float_fix > max_float/2)
        float_fix = float_fix - max_float;
    end
end
fprintf('%s -> %f\n',fix_num,float_fix);