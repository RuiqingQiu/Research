function K = computeArcCosineKernel(X,Y)

normX = sqrt(sum(X.*X));
normY = sqrt(sum(Y.*Y));
cosTh = (X'*Y)./(normX'*normY);
theta = abs(acos(cosTh));
K = (1/pi) * (normX'*normY) .* (sin(theta) + (pi-theta).*cosTh);
return;

