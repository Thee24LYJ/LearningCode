% MATLAB脚本：parse_dat_file_v6.m 
% 该脚本用于解析.dat文件，提取变量信息并将所有列的数据保存为.mat文件。
% 数据格式：
% // var1:1x10x0x8 var2:0x11x8x1 var3:1x8x0x3
% 3FF 000 121 002 3FF 000 121 002 123 12 23 34
% 3F0 000 121 002 3FF 000 121 002 123 22 28 74
% 1F0 100 131 202 5FF 010 121 002 123 32 23 24
% 定义输入文件路径
inputFilePath = 'input.dat';

% 打开文件进行读取
fid = fopen(inputFilePath, 'r');
if fid == -1
    error('无法打开文件：%s', inputFilePath);
end

% 读取第一行注释，提取变量信息
headerLine = fgetl(fid);
if ~startsWith(headerLine, '//')
    error('文件格式错误：第一行不是注释');
end

% 去掉注释符号和空格
headerLine = strtrim(headerLine(3:end));

% 分割变量定义
varDefs = split(headerLine);

% 初始化变量存储结构
vars = struct();

% 解析每个变量定义
for i = 1:length(varDefs)
    varDef = varDefs{i};
    parts = split(varDef, ':');
    if length(parts) ~= 2
        error('变量定义格式错误：%s', varDef);
    end
    
    % 提取变量名和参数
    varName = parts{1};
    params = split(parts{2}, 'x');
    if length(params) ~= 4
        error('变量参数格式错误：%s', varDef);
    end
    
    % 将参数转换为数值
    signed = str2double(params{1});
    totalBits = str2double(params{2});
    fractionalBits = str2double(params{3});
    numElements = str2double(params{4});
    
    % 存储变量信息
    vars.(varName).signed = signed;
    vars.(varName).totalBits = totalBits;
    vars.(varName).fractionalBits = fractionalBits;
    vars.(varName).numElements = numElements;
end

% 读取所有数据行
dataLines = {};
while ~feof(fid)
    dataLine = fgetl(fid);  % 逐行读取数据
    if ischar(dataLine)
        dataLines{end+1} = strtrim(dataLine);  % 去掉多余空格并存储
    end
end

% 关闭文件
fclose(fid);

% 将所有数据行合并成一个矩阵
dataArray = [];
for i = 1:length(dataLines)
    row = split(dataLines{i});  % 按空格分割每行数据
    dataArray = [dataArray; row'];  % 将每行数据转置后添加到矩阵中
end

% 确保数据矩阵的列数足够满足所有变量的需求
totalColumnsNeeded = 0;
for i = 1:length(varDefs)
    varDef = varDefs{i};
    parts = split(varDef, ':');
    varName = parts{1};
    totalColumnsNeeded = totalColumnsNeeded + vars.(varName).numElements;
end

if size(dataArray, 2) < totalColumnsNeeded
    error('数据列数不足：需要 %d 列数据，但只有 %d 列可用', totalColumnsNeeded, size(dataArray, 2));
end

% 遍历每个变量，解析数据并保存为.mat文件
currentColumn = 1;  % 当前列索引
for i = 1:length(varDefs)
    varDef = varDefs{i};
    parts = split(varDef, ':');
    varName = parts{1};
    numElements = vars.(varName).numElements;
    
    % 提取对应数量的列数据
    dataColumns = dataArray(:, currentColumn:currentColumn+numElements-1);  % 提取 numElements 列数据
    currentColumn = currentColumn + numElements;  % 更新当前列索引
    
    % 将数据转换为16进制数组（列向量形式）
    hexData = zeros(size(dataColumns, 1), numElements, 'uint16');  % 初始化存储矩阵
    for j = 1:numElements
        for k = 1:size(dataColumns, 1)
            hexData(k, j) = hex2dec(dataColumns{k, j});
        end
    end
    
    % 动态创建变量并保存为.mat文件
    eval([varName ' = hexData;']);  % 动态创建变量
    save([varName '.mat'], varName, '-v7.3');  % 保存为.mat文件
end

% 输出完成信息
disp('解析完成，数据已保存为.mat文件。');