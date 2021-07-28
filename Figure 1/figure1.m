clear;
clc;
close all;

K = [0:0.01:pi];
[KX,KY] = meshgrid(K);
t = 1;

figure('Renderer', 'painters', 'Position', [10 10 900 400])
set(gcf,'color','white')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot('position',[0.1,0.15,0.28,0.8]); hold on;
tperp = 1;
mu = 1;
Ek1 = 2*t*(cos(K)+cos(K)) + 2*tperp - mu;
Ek2 = 2*t*(cos(K)+cos(K)) - 2*tperp - mu;
FS1 = 2*t*(cos(KX)+cos(KY)) + 2*tperp - mu;
FS2 = 2*t*(cos(KX)+cos(KY)) - 2*tperp - mu;
plot(K/pi,Ek1,'-k','LineWidth',1);
plot(K/pi,Ek2,'-r','LineWidth',1);
plot(K/pi,zeros(size(K)),'--k','LineWidth',0.5);
ylabel('$\epsilon_\pm({\bf k})/t$','FontSize',30,'Interpreter','latex')
set(gca,'FontSize',25,'XTick',[0:0.25:1],'YTick',[-12:4:12],'LineWidth',1,'FontName','Times')
xticklabels({' \Gamma',' ',' ',' ','M '})
axis([0,1,-12,12])
string1 = ['$t_\perp = 1, t^\prime_\perp = 0$'];
string2 = ['$\mu = 1$     '];
text(0.04,10,'(b)','FontSize',25,'Interpreter','latex')
text(0.04,-8.5,string1,'FontSize',25,'Interpreter','latex')
text(0.04,-10.5,string2,'FontSize',25,'Interpreter','latex')
text(0.85,0,'$E_\mathrm{F}$','FontSize',25,'Interpreter','latex',...
     'BackgroundColor','white')

box on;

axes('position',[0.245,0.66,0.14*0.9,0.3*0.9]); hold on;
contour(KX/pi,KY/pi,FS1,[0 0],'-k','LineWidth',1);
contour(KX/pi,KY/pi,FS2,[0 0],'-r','LineWidth',1);
box on;
axis([0,1,0,1])
set(gca,'FontSize',25,'XTick',[-1:1:-1],'YTick',[-1:1:-1],'LineWidth',1)



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot('position',[0.4,0.15,0.28,0.8]); hold on;
tperp = 2;
mu = 1;
Ek1 = 2*t*(cos(K)+cos(K)) + 2*tperp - mu;
Ek2 = 2*t*(cos(K)+cos(K)) - 2*tperp - mu;
FS1 = 2*t*(cos(KX)+cos(KY)) + 2*tperp - mu;
FS2 = 2*t*(cos(KX)+cos(KY)) - 2*tperp - mu;
plot(K/pi,Ek1,'-k','LineWidth',1);
plot(K/pi,Ek2,'-r','LineWidth',1);
plot(K/pi,zeros(size(K)),'--k','LineWidth',0.5);
set(gca,'FontSize',25,'XTick',[0:0.25:1],'YTick',[-12:4:12],'LineWidth',1,'FontName','Times')
xticklabels({' \Gamma',' ',' ',' ','M '})
yticklabels({' ',' ',' ',' ',' ',' ',' '})
axis([0,1,-12,12])
box on;
string1 = ['$t_\perp = 2, t^\prime_\perp = 0$'];
string2 = ['$\mu = 1$     '];
text(0.04,10,'(c)','FontSize',25,'Interpreter','latex')
text(0.04,-8.5,string1,'FontSize',25,'Interpreter','latex')
text(0.04,-10.5,string2,'FontSize',25,'Interpreter','latex')

axes('position',[0.545,0.66,0.14*0.9,0.3*0.9]); hold on;
contour(KX/pi,KY/pi,FS1,[0 0],'-k','LineWidth',1);
contour(KX/pi,KY/pi,FS2,[0 0],'-r','LineWidth',1);
box on;
axis([0,1,0,1])
set(gca,'FontSize',25,'XTick',[-1:1:-1],'YTick',[-1:1:-1],'LineWidth',1)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot('position',[0.7,0.15,0.28,0.8]); hold on;
tperp = 2;
tperpp = 0.75;
mu = 1;
Ek1 = 2*(t+tperpp)*(cos(K)+cos(K)) + 2*tperp - mu;
Ek2 = 2*(t-tperpp)*(cos(K)+cos(K)) - 2*tperp - mu;
FS1 = 2*(t+tperpp)*(cos(KX)+cos(KY)) + 2*tperp - mu;
FS2 = 2*(t-tperpp)*(cos(KX)+cos(KY)) - 2*tperp - mu;
plot(K/pi,Ek1,'-k','LineWidth',1);
plot(K/pi,Ek2,'-r','LineWidth',1);
plot(K/pi,zeros(size(K)),'--k','LineWidth',0.5);
set(gca,'FontSize',25,'XTick',[0:0.25:1],'YTick',[-12:4:12],'LineWidth',1,'FontName','Times')
xticklabels({' \Gamma',' ',' ',' ','M '})
yticklabels({' ',' ',' ',' ',' ',' ',' '})
axis([0,1,-12,12])
box on;
string1 = ['$t_\perp = 2, t^\prime_\perp = 3/4$'];
string2 = ['$\mu = 1$     '];
text(0.04,10,'(d)','FontSize',25,'Interpreter','latex', 'BackgroundColor','white')
text(0.04,-8.5,string1,'FontSize',25,'Interpreter','latex')
text(0.04,-10.5,string2,'FontSize',25,'Interpreter','latex')

axes('position',[0.845,0.66,0.14*0.9,0.3*0.9]); hold on;
contour(KX/pi,KY/pi,FS1,[0 0],'-k','LineWidth',1);
contour(KX/pi,KY/pi,FS2,[0 0],'-r','LineWidth',1);
box on;
axis([0,1,0,1])
set(gca,'FontSize',20,'XTick',[-1:1:-1],'YTick',[-1:1:-1],'LineWidth',1)

saveas(gcf,'Bands.eps','epsc')