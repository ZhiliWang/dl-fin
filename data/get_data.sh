%I created this simple script

startDate='Jan-01-2006';
endDate='Jun-21-2017';
symbol='KO';
defaultdownloadsfolder = '~/zhiliwang/Documents/fin'; % need to change to your default download folder
cookiecode = 'XXXXXXXXXXX'; %find your cookie code. I am using chrome and all works.
%example https://query1.finance.yahoo.com/v7/finance/download/%5EDJI?period1=1495460641&period2=1498139041&interval=1d&events=history&crumb=XXXXXXXXXXX

end_datenum = (datenum(endDate) - datenum('Jan-01-1970')) * 86400; %today
start_datenum = (datenum(startDate) - datenum('Jan-01-1970')) * 86400;
startDateStr = num2str(start_datenum);
endDateStr = num2str (end_datenum);

link=['https://query1.finance.yahoo.com/v7/finance/download/',symbol ,'?period1=',startDateStr,'&period2=',endDateStr,'&interval=1d&events=history&crumb=',cookiecode];
web(link,'-browser')

filename = [defaultdownloadsfolder,'\',symbol,'.csv'];

fileID = fopen(filename,'r');
pause(1);
dataArray = textscan(fileID,'%s%f%f%f%f%f%*s%[^\n\r]', 'Delimiter', ',', 'EmptyValue' ,NaN,'HeaderLines' ,1, 'ReturnOnError', false);
fclose(fileID);

Date = dataArray{:, 1};
DateTime = datetime(Date, 'InputFormat', 'yyyy-MM-dd');
Open = dataArray{:, 2};
High = dataArray{:, 3};
Low = dataArray{:, 4};
Close = dataArray{:, 5};
AdjClose = dataArray{:, 6};