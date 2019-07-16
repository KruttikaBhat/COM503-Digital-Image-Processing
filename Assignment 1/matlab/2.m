numImg=100;
size=512;
lena512= imread('lena512.bmp');

J=zeros(size,size,numImg); 
for i=1:numImg
    J(:,:,i)= imnoise(lena512,'gaussian');
end

avg=zeros(size,size);

for i=1:numImg
    avg=avg+J(:,:,i);
end
avg=avg/numImg;

avg1=uint8(avg);

lena2=imnoise(avg1,'salt & pepper');
figure, imshow(lena2);


output=zeros(512,512);
output1=zeros(512,512);
output2=zeros(512,512);
output(1,:)=lena2(1,:);
output(:,1)=lena2(:,1);
output(512,:)=lena2(512,:);
output(:,512)=lena2(:,512);


for s=2:511
    for t=2:511
        median3=zeros(1,9);
        for i=s-1:s+1
            for j=t-1:t+1 
                count=1;
                while lena2(i,j)<median3(count)
                    count=count+1;
                end
                for k=9:-1:count+1
                    median3(k)=median3(k-1);
                end
                median3(count)=lena2(i,j);
            end
        end 
        output(s,t)=median3(5);
    end
end

figure, image(output);

colormap(gray(256));


output1(1:2,:)=lena2(1:2,:);
output1(:,1:2)=lena2(:,1:2);
output1(511:512,:)=lena2(511:512,:);
output1(:,511:512)=lena2(:,511:512);

for s=3:510
    for t=3:510
        count=1;
        median5=zeros(1,25);
        for i=s-2:s+2
            for j=t-2:t+2 
                count=1;
                while lena2(i,j)<median5(count)
                    count=count+1;
                end
                for k=25:-1:count+1
                    median5(k)=median5(k-1);
                end
                median5(count)=lena2(i,j);
            end
        end 
        output1(s,t)=median5(13);
    end
end

figure, image(output1);
colormap(gray(256));

output2(1:3,:)=lena2(1:3,:);
output2(:,1:3)=lena2(:,1:3);
output2(510:512,:)=lena2(510:512,:);
output2(:,510:512)=lena2(:,510:512);

for s=4:509
    for t=4:509
        count=1;
        median7=zeros(1,49);
        for i=s-3:s+3
            for j=t-3:t+3 
                count=1;
                while lena2(i,j)<median7(count)
                    count=count+1;
                end
                for k=49:-1:count+1
                    median7(k)=median7(k-1);
                end
                median7(count)=lena2(i,j);
            end
        end
        output2(s,t)=median7(25);
    end
end
    
figure, image(output2);
colormap(gray(256));
    