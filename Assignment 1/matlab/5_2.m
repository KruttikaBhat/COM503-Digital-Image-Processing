test=imread('pout-dark.jpg');
ref=imread('pout-bright.jpg');

figure, imshow(test);
figure, imshow(ref);

testfreq=zeros(256,1);
reffreq=zeros(256,1);

for i=1:size(test,1)
    for j=1:size(test,2)
        for k=1:size(test,3)
            testfreq(test(i,j,k)+1)=testfreq(test(i,j,k)+1)+1;
        end
    end
end


for i=1:size(ref,1)
    for j=1:size(ref,2)
        for k=1:size(ref,3)
            reffreq(ref(i,j,k)+1)=reffreq(ref(i,j,k)+1)+1;
        end
    end
end


testfp=testfreq/sum(testfreq);
testcum=testfp;

reffp=reffreq/sum(reffreq);
refcum=reffp;

for i=2:size(testcum,1)
    testcum(i)=testcum(i)+testcum(i-1);
    refcum(i)=refcum(i)+refcum(i-1);
end

stest=round(testcum.*255);
sref=round(refcum.*255);

output=zeros(size(test),class(test));
match=zeros(1,256);

%sref


for i=1:256
    val=sref(i);
    min=257;
    index=256;
    for j=1:256
        if abs(val-stest(j))<=min
            min=abs(val-stest(j));
            index=j;
        else
            break;
        end
        
    end
    match(i)=index;
end
match;

for i=1:size(output,1)
    for j=1:size(output,2)
        for k=1:size(output,3)
            output(i,j,k)=match(test(i,j,k)+1);
        end
    end
end

%output

figure, image(output);
colormap(gray(256));
