% 二进制字符串转换为16进制数：
% 方法1：基本转换
bin_str = '110110101011';
dec_num = bin2dec(bin_str);   % 二进制转十进制
hex_str = dec2hex(dec_num);   % 十进制转十六进制

disp(['二进制: ', bin_str]);
disp(['十六进制: ', hex_str]);
% 输出: 二进制: 110110101011
%       十六进制: DAB
