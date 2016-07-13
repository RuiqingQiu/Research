%%%%%%%%%%%%%%%%%%

function idx = createConvolveLayer(n,d)

idx = zeros(n,n,d^2);
for i=1:n
  for j=1:n
    x = repmat(j:j+d-1,1,d);
    y = reshape(repmat(i:i+d-1,d,1),1,d^2);
    idx(i,j,:) = sub2ind([n+d-1 n+d-1],x,y);
  end
end
return

%%%%%%%%%%%%%%%%%%



