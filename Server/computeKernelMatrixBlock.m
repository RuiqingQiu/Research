function K = computeKernelMatrixBlock(A,B)

% NETWORK
n0 = 32; 
n1 = 28; 
n2 = 14;
n3 = 10;
n4 = 5;
d1 = 5;
d3 = 5;

% LOCALLY CONNECTED LAYERS
idx1 = createConvolveLayer(n1,d1);
idx2 = createSubsampleLayer(n2);
idx3 = createConvolveLayer(n3,d3);
idx4 = createSubsampleLayer(n4);

% ALLOCATE KERNEL MATRIX
nA = size(A,1);
nB = size(B,1);
K = zeros(nA,nB);

% COMPUTE ELEMENTS
if (isequal(A,B)) % MATRIX IS SYMMETRIC
  for i=1:nA
    for j=1:i
      K(i,j) = computeLeKernel(A(i,:,:),B(j,:,:),idx1,idx2,idx3,idx4);
      K(j,i) = K(i,j);
    end
  end
else
  for i=1:nA
    for j=1:nB
      K(i,j) = computeLeKernel(A(i,:,:),B(j,:,:),idx1,idx2,idx3,idx4);
    end
  end
end
