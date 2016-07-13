%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [images,labels] = loadAllMNIST32x32(imageF,labelF)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% LABELS
% tic;
fid = fopen(labelF,'r');
labelHeaderSize = 8;
header = fread(fid,labelHeaderSize,'uchar');
labels = fread(fid,inf,'uchar');
fclose(fid);
nImage = length(labels);

% IMAGES
cropped = 28;
padded = 32;
offset = 2;
nPixel = cropped*cropped;
images = zeros(nImage,padded,padded);

% SLURP
% colormap hot;
fid = fopen(imageF,'r','b');
imageHeaderSize = 16;
header = fread(fid,imageHeaderSize,'uchar');
for ii=1:nImage
  img = fread(fid,nPixel,'uchar');
  img = reshape(img,cropped,cropped)'/255.0;
  images(ii,1+offset:end-offset,1+offset:end-offset) = img;
  % imagesc(images(:,:,ii)); axis equal tight square; drawnow;
end;
fclose(fid);
% toc;
return;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



