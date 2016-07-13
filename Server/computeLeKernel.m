%%%%%%%%%%%%%%%%%%%%%%%%%%

function kAB = computeLeKernel(A,B,idx1,idx2,idx3,idx4)

% LAYERS
n0 = size(A,1);
n1 = size(idx1,1);
n2 = size(idx2,1);
n3 = size(idx3,1);
n4 = size(idx4,1);

% COMPUTE
k0 = A.*B; u0 = abs(A); v0 = abs(B);
[k1,u1,v1] = convolve(n1,k0,u0,v0,idx1);
[k2,u2,v2] = subsample(n2,k1,u1,v1,idx2);
[k3,u3,v3] = convolve(n3,k2,u2,v2,idx3);
[k4,u4,v4] = subsample(n4,k3,u3,v3,idx4);
kAB = arcCosKernel(sum(k4(:)),norm(u4(:)),norm(v4(:))); % FULL
return;

%%%%%%%%%%%%%%%%%%%%%%%%%%

function kk = arcCosKernel(k,u,v)

cosT = real(k./(u.*v+realmin));
sinT = real(sqrt(1-cosT.^2));
kk = (u.*v/pi) .* (sinT + (pi-real(acos(cosT))).*cosT);
return;

%%%%%%%%%%%%%%%%%%%%%%%%%%

function [kk,uu,vv] = convolve(n,k,u,v,idx)
  
kk = zeros(n);
uu = zeros(n);
vv = zeros(n);
for i=1:n
  ki = sum(k(idx(i,:,:)),3);
  uu(i,:) = sqrt(sum(u(idx(i,:,:)).^2,3));
  vv(i,:) = sqrt(sum(v(idx(i,:,:)).^2,3));
  kk(i,:) = arcCosKernel(ki,uu(i,:),vv(i,:));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%

function [kk,uu,vv] = subsample(n,k,u,v,idx)
  
kk = zeros(n);
uu = zeros(n);
vv = zeros(n);
for i=1:n
   kk(i,:) = sum(k(idx(i,:,:)),3);
   uu(i,:) = sqrt(sum(u(idx(i,:,:)).^2,3));
   vv(i,:) = sqrt(sum(v(idx(i,:,:)).^2,3));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
