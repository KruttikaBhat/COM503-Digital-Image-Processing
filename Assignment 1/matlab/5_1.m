img=imread('pout-dark.jpg');
figure, imshow(img);

freq=zeros(256,1);
size(img);

for i=1:size(img,1)
    for j=1:size(img,2)
        for k=1:size(img,3)
            freq(img(i,j,k)+1)=freq(img(i,j,k)+1)+1;
        end
    end
end
%freq
freqprob=freq/sum(freq);
cum=freqprob;


for i=2:256
    cum(i)=cum(i)+cum(i-1);
end
cum;
s=round(cum.*255);

equ=img;


for i=0:255
    for j=1:size(img,1)
        for k=1:size(img,2)
            for l=1:size(img,3)
                if img(j,k,l)==i
                    equ(j,k,l)=s(i+1);
                end
            end
        end
    end
end
% 
% for i=1:size(img,1)
%     for j=1:size(img,2)
%         for k=size(img,3)
%             equ(i,j,k)=s(img(i,j,k)+1);
%         end
%     end
% end



%equ
figure, image(equ);
colormap(gray(256));