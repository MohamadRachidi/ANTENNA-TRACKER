%This Code was Written By Nemeen Shah
%Subscribe to My YouTube Channel: https://Youtube.com/NematicsLab

%Size of PCB
pcbThickness = 1.6e-3;  %1.6mm
pcbLength = 152.4e-3;   %152.4mm or 6inch
pcbWidth = 101.6e-3;    %101.6mm 0r 4inch

%Specifying Material of PCB
pcbMaterial = 'FR4';
pcbEpsilonR = 4.4;

%Creating dielectic Material
d = dielectric(pcbMaterial); %Creating dielectic Material
d.EpsilonR = pcbEpsilonR;
d.Thickness = pcbThickness;


GndPlane = antenna.Rectangle('Length',pcbLength,'Width',pcbWidth); %Creating Ground Plane of Antenna
AntennaPlane=antenna.Rectangle('Length',5e-2,'Width',1e-2,'Center',[0,0]); %Creating Feed Plane of Antenna 

%Creating Different Shapes of antenna
p = pcbStack;
p.Name = 'Strip-fed slot';
p.BoardShape = GndPlane;
p.BoardThickness = pcbThickness;
p.Layers = {AntennaPlane,d,GndPlane};
p.FeedLocations = [0,0,1,3]; %[x Cordinate,y Cordinate,startLayer stopLayer]

p.Layers = {AntennaPlane,d,GndPlane};

%%Creating PCB Stack
figure(1);
show(p); %Display Antenna 

figure(2);
pattern(p,1.82e9);  %Display Radiation Pattern at 1.943GHZ

figure(3);
impedance(p,1.6e9:2e7:2.2e9);   %Display Impedance Graph from 1.6GHz to 2.2GHz

freq = linspace(1.6e9, 2.2e9, 50); % Creating Frequency Vector
s = sparameters(p,freq,50); % Calalculate S11 for all frequencys

figure(4);
rfplot(s);%Diplay S11 Plot

%Generating Gerber Files for Fabrication 
C = PCBConnectors.SMA_Cinch;
W = PCBServices.PCBWayWriter;
W.Filename = 'antenna_design_example';

gerberWrite(p,W,C);

%This will genrate a ZIP file in your project folder with Name "antenna_design_Example.zip"
%Now just Upload the Gerber file to any PCB Service online and you are ready to go

%Else if you want to make PCB Yourself then upload the files to https://www.gerber-viewer.com/
%from there you can conver the gerber into PDF and take print of all individual layers
 
