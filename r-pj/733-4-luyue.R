x<-seq(-4*pi,4*pi,0.1)
y<-sin(x)
plot(x,y,type="b")

t<-rnorm(40)
t
t<-sort(t,decreasing=T)
t
which.max(t)
max(t)
mean(t)
median(t)
boxplot(t)

A<-matrix(c(1,3,3,3,3,2,3,3,3,3,3,3,3,3,3,4),ncol=4,byrow=T)
det(A)
nrow(A)
ncol(A)
B<-t(A)
B
A%*%B

C<-diag(1:4)

b<-1:4
x<-solve(A,b)
View(x)

iris.1<-iris[iris[1]>5,]
iris.1

white<-read.csv("white.csv", sep=";")
typeof(white)
unique(white["quality"])
colnames(white)[12]<-"yf"
box(white[1],white["yf"])
f<-function(x){
	if(x > 1)
	{
		2 * x^2 + 1
	}
	else
	{
		3 * x
	}
}
f(1)+2*f(3)
x<-seq(-5,5,0.1)
plot(x,sapply(x, f),main = "the plot of f",type = "l",col="red")
matrix(sapply(1:10000, function(i){0.4^abs(i%%100-i%/%100-1)}),nrow=100)

