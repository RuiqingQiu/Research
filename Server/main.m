% TRAINING DATA
imageF = 'train-images-idx3-ubyte';
labelF = 'train-labels-idx1-ubyte';
[trImages,trLabels] = loadAllMNIST32x32(imageF,labelF);

% WHICH DIGITS
digitA = 0;
digitB = 0;
A = trImages(find(trLabels==digitA),:,:);
B = trImages(find(trLabels==digitB),:,:);
A = A(1:100,:,:);
B = B(1:100,:,:);

% COMPUTE
tic;
K = computeKernelMatrixSublock(A,B);
toc;

% SAVE
fileName = sprintf('K_%dvs%d.txt',digitA,digitB);
save(fileName,'K','-ascii','-double');

