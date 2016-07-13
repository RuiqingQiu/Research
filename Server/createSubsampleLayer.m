%%%%%%%%%%%%%%%%%%%%%%

function idx = createSubsampleLayer(n)

% subsample by 2
idx = zeros(n,n,2^2);
for i=1:n
  for j=1:n
    x = [2*j-1 2*j 2*j-1 2*j];
    y = [2*i-1 2*i-1 2*i 2*i];
    idx(i,j,:) = sub2ind([2*n 2*n],x,y);
  end
end
return

%%%%%%%%%%%%%%%%%%%%%%