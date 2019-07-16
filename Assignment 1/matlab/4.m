img = imread('camman.jpg');
figure, imshow(img);

scaler=0.5;
scalec=0.5;
rin=size(img,1);
cin=size(img,2);
rout=floor(rin*scaler);
cout=floor(cin*scalec);
% rout=200;
% cout=200;
% scaler=rout/rin;
% scalec=cout/cin;

%nearest neighbor
r=zeros(rout,1);
c=zeros(cout,1);

nn=zeros(rout,cout);

for i=1:rout
    if scaler<1
        r(i)=ceil(i/scaler);
    else
        r(i)=floor(i/scaler);
    end
    if r(i)<1
        r(i)=1;
    end
    if r(i)>rin
            r(i)=rin;
    end
end
for i=1:cout
    if scalec<1
        c(i)=ceil(i/scalec);
    else
        c(i)=floor(i/scalec);
    end
    if c(i)<1
        c(i)=1;
    end
    if c(i)>cin
            c(i)=cin;
    end
end

for i=1:rout
    for j=1:cout
        nn(i,j)=img(r(i),c(j));
    end
end

figure, image(nn);
colormap(gray(256));

%bilinear interpolation

bi=zeros(rout,cout);

for i=1:rout
    r(i)=i;
end
for i=1:cout
    c(i)=i;
end


rf=r./scaler;
cf=c./scalec;


r0=floor(rf);
c0=floor(cf);

deltar=rf-r0;
deltac=cf-c0;

for i=1:rout
    for j=1:cout
        if r0(i)<512 && c0(j)<512 && r0(i)>0 && c0(j)>0
            p1=img(r0(i),c0(j))*(1-deltar(i))+img(r0(i)+1,c0(j))*deltar(i);
            p2=img(r0(i),c0(j)+1)*(1-deltar(i))+img(r0(i)+1,c0(j)+1)*deltar(i);
            bi(i,j)=p1*(1-deltac(j))+p2*deltac(j);
        else
            bi(i,j)=img(round(i/scaler),round(j/scalec));
        end
    end
end

figure, image(bi);
colormap(gray(256));





