numImg=100;
size=512;
lena512= imread('lena512.bmp');
figure, imshow(lena512);

%x=size(lena512)
J=zeros(size,size,numImg); 
for i=1:numImg
    J(:,:,i)= imnoise(lena512,'gaussian');
end

avg=zeros(size,size);

for i=1:numImg
    avg=avg+J(:,:,i);
end
avg=avg/numImg;
figure, image(avg);
colormap(gray(256));