# 数学
![image](/model.png)
* c为中心词序号
* m为窗口大小
* 词向量长度为100
* $i\in[0,100),N$代表词向量
* $j,V$代表词典大小
* $h_{1*N}\qquad W'_{N*V}\qquad y_{1*V}\qquad r_{1*V}\qquad t_{1*V}$
$$h=\sum_{i=c-m}^{c+m}w_i$$
$$y=h*W'$$
$$y_i=\sum_jh_j*b_{ji}$$
$$r=softmax(y)$$
$$softmax(x_i)=\frac{e^{x_i}}{\sum_ie^{x_i}}$$
$$L=-\sum_it_i\ln r_i$$
$$\frac{\partial L}{\partial r_k}=\frac{\partial -\sum_kt_k\ln r_k}{\partial r_k}=-\frac{t_k}{r_k}$$
$$\frac{\partial r_k}{\partial y_i}=\frac{\partial \frac{e^{y_k}}{\sum_ke^{y_k}}}{\partial y_i}$$
对于不同k与i:
* 当$k\not = i$时
  $$\frac{\partial r_k}{\partial y_i}=-\frac{e^{y_k}e^{y_i}}{{\sum_ke^{y_k}}^2}=-r_kr_i$$
* 当$k=i$时:
  $$\frac{\partial r_k}{\partial y_i}=\frac{\partial r_i}{\partial y_i}=\frac{\partial \frac{e^{y_i}}{\sum_ke^{y_k}}}{\partial y_i}=\frac{e^{y_i}\sum_ke^{y_k}-e^{y_i}e^{y_i}}{(\sum_ke^{y_k})^2}=r_i(1-r_i)$$
$$\frac{\partial r_k}{\partial y_i}=\begin{cases}
-r_kr_i,k\not =i\\
r_i(1-r_i),k=i
\end{cases}$$
$$\begin{aligned}
\frac{\partial L}{\partial y_i}&=\sum_k\frac{\partial L}{\partial r_k}\frac{\partial r_k}{\partial y_i}\\
&=\sum_k-\frac{t_k}{r_k}\frac{\partial r_k}{\partial y_i}\\
&=-\frac{t_i}{r_i}r_i(1-r_i)+\sum_{k,k\not = i}-\frac{t_k}{r_k}(-r_kr_i)\\
&=t_i(r_i-1)+\sum_{k,k\not =i}t_kr_i\\
&=t_ir_i-t_i+\sum_{k,k\not =i}t_kr_i\\
&=\sum_kt_kr_i-t_i\\
&=r_i\sum_kt_k-t_i
\end{aligned}
$$
由于标准向量只有一个为1，其余都是0。显然，$\sum_kt_k=1$。
$$\frac{\partial L}{\partial y_i}=r_i-t_i$$
$$\frac{\partial y_i}{\partial b_{ji}}=\frac{\partial \sum_jhj*b_{ji}}{\partial b_{ji}}=h_j$$
$$\frac{\partial y_i}{\partial h_j}=b_{ji}$$
$$\frac{\partial L}{\partial b_{ji}}=\sum_k\frac{\partial L}{\partial y_k}\frac{\partial y_k}{\partial b_{ji}}=\frac{\partial L}{\partial y_i}\frac{\partial y_i}{\partial b_{ji}}=(r_i-t_i)h_j$$
$$\frac{\partial L}{\partial h_j}=\sum_k\frac{\partial L}{\partial y_k}\frac{\partial y_k}{\partial h_j}=\sum_k(r_k-t_k)b_{jk}$$
写为矩阵形式:
$$\Delta W'= (r-t)^T*h$$
$$\Delta h=(\sum_k(r_k-t_k))*W'*ones(V,1)$$