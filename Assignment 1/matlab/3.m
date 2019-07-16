im1=imread('pisa.jpg');
figure, imshow(im1);
[m,n]=size(im1);
theta = 5*pi/180;
mm = m*sqrt(2);
nn = n*sqrt(2);
for i=1:mm
   for j=1:nn
      p = uint16((i-mm/2)*cos(theta)+(j-nn/2)*sin(theta)+m/2);
      q = uint16(-(i-mm/2)*sin(theta)+(j-nn/2)*cos(theta)+n/2);
      if p>0 && q>0 && p<=m && q<=n           
         im2(i,j)=im1(p,q);
      end
   end
end
figure;
imshow(im2);