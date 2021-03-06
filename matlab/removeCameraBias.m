clc;
clear;

USE_SIX = true;

sourceFolder = 'data/exp_3/';
load(strcat(sourceFolder,'originalData.mat'))
destinationFolder = 'data/exp_3_debiased/';
Wn=0.025;
[b,a]=butter(5,Wn,'low');
delD = 0.01;
%%% Fitting the "true zero"/ debias the data
%%%
%fit a 2-piece function for the force-displacement data
%
%            /
%           /
%          /
%----------
%so the curve end up like this.
%The seond curve is a 4th order polynomial.. potentially get this to 4th
%order...
%a few things:
%-put less weight on the error with the first piece
%-intercept can be a decision variable or just set to be 0..
%or based on observation.. intercept should be a bounded closely
%-decision variables need to be scaled.. (especially the x-position..)


%the decision variables are not scaled properly..
%x(1) has too big of a range.. this might actually pose difficulties 
%to the algorithm
scale = 0.1;

%%use 6 decision variables..
if USE_SIX
%works for exp_1&4
% x0 = [3;0;1;0;0;0];
% x0Prime = [1;0;0;0;0;0];
% lb=[-10;-0.1;-5;-5;-5;-5];
% ub=[1;0.1;5;5;5;5];

% exp3 lamb has very sharp curves
x0 = [-2;0;1;0;0;0];
x0Prime = [2;0;1;0;0;0];

lb=[-9;-0.1;-5;-5;-5;-5];
ub=[4;0.1;10;5;5;5];
else
% exp3 lamb has very sharp curves
x0 = [-2;0;1;0;0;0];
x0Prime = [2;0;1;0;0;0];

lb=[-10;-0.1;-5;-5;-5;-5];
ub=[3;0.1;10;5;5;5];  
end

%MODE = 0;%calculate
%MODE = 1;%plot
MODE = 2;%icp

%perform scaling..
x0(1) = x0(1)*scale;
lb(1)= lb(1)*scale;
ub(1)= ub(1)*scale;
if MODE == 0
    errorThreshold = 35;
    displacementBias = [];
    fittedCoefficients = [];
%     %for i=1:1:size(probedPoints,1)
%     for i=34:1:40
%     %for i=[6]
%     %for i=size(probedPoints,1):-1:1
%             forceData = dlmread(strcat(sourceFolder,'point/force_',num2str(i-1),'.txt'),' ');
%             forceData = forceData(:,[5 4]);
%             forceData(:,1) = forceData(:,1)*1000;
%             
%             if USE_SIX
%                 %try 3 different methods
%                 options = optimoptions('fmincon','Algorithm','interior-point','Display','none');
%                 [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);
%                 if fval > errorThreshold
%                     options = optimoptions('fmincon','Algorithm','sqp','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);           
%                 end  
%                 if fval>errorThreshold
%                     options = optimoptions('fmincon','Algorithm','active-set','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);
%                 end
% 
% 
%                 %try different initial values with different methods
%                 options = optimoptions('fmincon','Algorithm','interior-point','Display','none');
%                 [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0Prime,[],[],[],[],lb,ub,[],options);
%                 if fval > errorThreshold
%                     options = optimoptions('fmincon','Algorithm','sqp','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0Prime,[],[],[],[],lb,ub,[],options);           
%                 end  
% 
%                 if fval>errorThreshold
%                     options = optimoptions('fmincon','Algorithm','active-set','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc(x,forceData,scale),x0Prime,[],[],[],[],lb,ub,[],options);
%                 end
%             
%             else
%                 
%                 options = optimoptions('fmincon','Algorithm','interior-point','Display','none');
%                 [x,fval]=fmincon(@(x)objectFunc3(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);
%                 if fval > errorThreshold
%                     options = optimoptions('fmincon','Algorithm','sqp','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc3(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);           
%                 end  
%                 if fval>errorThreshold
%                     options = optimoptions('fmincon','Algorithm','active-set','Display','none');
%                     [x,fval]=fmincon(@(x)objectFunc3(x,forceData,scale),x0,[],[],[],[],lb,ub,[],options);
%                 end
%             end
%             
%             
%             
%             %if still fail... try different objective function
% %             if fval>errorThreshold
% %             options = optimoptions('fmincon','Algorithm','sqp','Display','none');
% %             [x,fval]=fmincon(@(x)objectFunc2(x,forceData,scale),x0Prime,[],[],[],[],lb,ub,[],options);
% %             end
%             
%             %scale it back..
%             x(1) = x(1)/scale;
%             %if fval > errorThreshold
%                 i
%                 x
%                 fval   
%                 Y=[];
%                 if USE_SIX
%                     for j=1:1:size(forceData(:,1),1)
%                         Y=[Y;forceModel(forceData(j,1),x)];
%                     end
%                 else
%                     for j=1:1:size(forceData(:,1),1)
%                         Y=[Y;forceModel2(forceData(j,1),x)];
%                     end
%                 end
%                 figure
%                 plot(forceData(:,1),forceData(:,2),'b')%,forceData(:,1),filteredF,'r')
%                 hold on
%                 h1 = plot(forceData(:,1),Y,'r');
%                 if USE_SIX
%                     h2 = plot(x(1),x(2),'g.','MarkerSize',20);
%                 else
%                     h2 = plot(x(1),0,'g.','MarkerSize',20);
%                 end
%                 legend([h1,h2],{'fitted line','bias'})
%                 title(strcat('force-displacement at point',{' '},num2str(i)))
%                 xticks([-5 -4.5 -4 -3.5 -3 -2.5 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5])
%                 xticklabels({'-5','-4.5','-4','-3.5','-3','-2.5','-2','-1.5','-1','-0.5','0','0.5','1',...
%                     '1.5','2','2.5','3','3.5','4','4.5','5'})
%             %end
%             displacementBias = [displacementBias;x(1)];
%             fittedCoefficients = [fittedCoefficients;x(end-3:end).'];
%             
%     end


    %For the shoe(exp4).. there are still unsatisfactory points.. fix them manually
%     displacementBias(94) = -0.7;
%     displacementBias(90) = -0.5;

    
    %for exp_2, the sloth...
%     displacementBias(87) = -0.9;
%     displacementBias(77) = -2.5;
%     displacementBias(74) = 0;
%     displacementBias(64) = 0;
%     displacementBias(56) = -0.6;
%     displacementBias(21) = -4.5;
%     displacementBias(3) = -1;

%     %for exp_1
%     displacementBias(112) = 2.5;
%     displacementBias(109) = 0.8;
%     displacementBias(108) = 1;
%     displacementBias(84) = 4;
%     displacementBias(83) = -1;
%     displacementBias(82) = 1.5;
%     displacementBias(80) = -4;
%     displacementBias(77) = 0.5;
%     displacementBias(32) = 6;
%     displacementBias(24) = 2.5;
%     displacementBias(21) = 3;
%     displacementBias(20) = 0;
%     displacementBias(7) = 0;
%     displacementBias(17) = 1;
    
    %for exp_3
    displacementBias = [-3;-2.5;-1.8;-2.75;-3.7;-2.5;-2.5;-4.2;-6;-1.7;...
        -2;-1.5;-1.75;-2.5;-3;-1;0.25;-3;-2;-3.5;...
        -3;1.5;-4.5;-2.5;-3.5;-1.5;-4.1;-4.4;-2;-3.75;...
        -4.3;-2.9;-3;5.7;-4;-3.5;0.5;-2.5;-2.3;-2.5;...
        -3.5;-4.2;-3.5;-2;-0.2;-4;-1.4;0;-4.8;-2.5;...
        2.5;-1.5;-4.5;-2.7;-0.5;-2;0.15;0.1;-3;-1.25;...
        -1.8;-2.3;-4;-1.5;1.1;-0.5;-3.5;-2;0.5;0;...
        -2;0;-3.1;-1.5;1.5;-0.5;-0.5;-4.5;-0.8;-1.8;...
        -1;-1;-0.5;1.7;0.5;0.8;1;1;1.5;0.5;...
        3.6;0.5;3.5;4];
    save(strcat(sourceFolder,'pointBias.mat'),'displacementBias','fittedCoefficients')
end



%% 2D bias map
if MODE == 1
    load(strcat(sourceFolder,'pointBias.mat'));
    
    queryDisplacement = 0.005;
    xRange =[-0.02 0.25];
    yRange =[-0.01 0.25];
    colorBias = -10;
    colorScale = 20;
    colormap(hsv)
    for i = 1:1:size(probedPoints,1) 
    %for i=[17,87]
        x = probedPoints(i,1)-bias(1);
        y = probedPoints(i,2)-bias(2);
        BBias = displacementBias(i);
        BBias = (BBias-colorBias)/colorScale;
        if BBias > 1
            BBias = 1;
        elseif BBias < 0
            BBias = 0;
        end      
        plot(x,y,'.','Color',hsv2rgb([BBias,1,1]),'MarkerSize',20)
        hold on
    end
    axis equal
    axis([xRange yRange])
    xlabel('x (m)')
    ylabel('y (m)')
    hc = colorbar;
    set(hc,'TickLabels',{'-10 mm','-8 mm','-6 mm','-4 mm','-2 mm','0 mm',...
    '2 mm','4 mm','6 mm','8 mm','10 mm'});
    title('Bias at the Probed Points')
    
    


% dispList =2:0.5:3;%change this to mm's
% for i=1:1:size(dispList,2)
%     figure
%     xRange =[-0.02 0.1];
%     yRange =[-0.01 0.16];
%     colorBias = -0.5;
%     colorScale = 2 ;
%     colormap(hsv)
%     for j=1:1:size(probedPoints,1)
%         %first predict force with the fitted polynomial
%         disp = dispList(i);
%         force = dot(fittedCoefficients(j,:),[disp,disp^2,disp^3,disp^4]);
%         x = probedPoints(j,1)-bias(1);
%         y = probedPoints(j,2)-bias(2);
%         force = (force-colorBias)/colorScale;
%         if force > 1
%             force = 1;
%         elseif force < 0
%             force = 0;
%         end      
%         plot(x,y,'.','Color',hsv2rgb([force,1,1]),'MarkerSize',10)
%         hold on
%     end
%     axis equal
%     axis([xRange yRange])
%     xlabel('x (m)')
%     ylabel('y (m)')
%     hc = colorbar;
%     set(hc,'TickLabels',{'-9.5 mm','-8.7 mm','-7.9 mm','-7.1 mm','-6.3 mm','-5.5 mm',...
%     '-4.7 mm','-3.9 mm','-3.1 mm','-2.3 mm','-1.5 mm'});
%     title('Bias at the Probed Points')
% end


end

if MODE == 2 %try ICP..
    %pcd = dlmread(strcat('data/exp_3/','originalPcd.txt'),' ');
    %probedPoints = dlmread(strcat('data/exp_3/','probePcd_theta.txt'),' ');
    %pcshowpair(pointCloud(diluteData(pcd(:,1:3),1)),pointCloud(probedPoints(:,1:3)),'MarkerSize',40);
    
    figure
    xRange =[-0.02 0.1];
    yRange =[-0.01 0.16];    
    load(strcat(sourceFolder,'pointBias.mat')) %%The bias is in mm
    tactilePoints=[];
    for i=1:1:size(probedPoints,1)
        pt = probedPoints(i,1:3);
        normal = probedPoints(i,7:9);
        ptNew = pt - (displacementBias(i)/1000)*normal;
        tactilePoints = [tactilePoints;ptNew];
    end
    %to ensure convergence of icp.. use tactile points as fixed points..
    moving = pointCloud(tactilePoints);
    fixed = pointCloud(diluteData(pcd(:,1:3),1));
    [tform,movingReg,rmse] = icp(moving,fixed,'MaxIterations',30,'Verbose',...
        true,'Metric','pointToPoint')%,'Tolerance',[0.001,0.005]);
    transform = invert(tform);
    %transform the pcd
    %newVisualPcd  = fixed;
    newVisualPcd = pctransform(fixed,transform);
    pcd(:,1:3) = newVisualPcd.Location;
    save(strcat(sourceFolder,'ICPTransform.mat'),'transform')
    %display pcd
    %pcshow(moving)
    %pcshowpair(movingReg,fixed,'MarkerSize',40)
    %% Plot the error after registration
    Ds = [];
    colorBias = 0;
    colorScale =4;
    colormap(hsv)
    for i=1:1:size(tactilePoints,1)
        [Idx,D] = knnsearch(newVisualPcd.Location,tactilePoints(i,:),'K',1);
        color = (D*1000-colorBias)/colorScale;
        if color > 1
            color = 1;
        elseif color < 0
            color = 0;
        end  
        pt = newVisualPcd.Location(Idx,:);
        x = pt(1) - bias(1);
        y = pt(2) - bias(2);
        plot(x,y,'.','Color',hsv2rgb([color,1,1]),'MarkerSize',10)
        hold on
        Ds = [Ds;D];
    end
    axis equal
    axis([xRange yRange])
    xlabel('x (m)')
    ylabel('y (m)')
    hc = colorbar;
    set(hc,'TickLabels',{'0 mm','0.4 mm','0.8 mm','1.2 mm','1.6 mm','2.0 mm',...
    '2.4 mm','2.8 mm','3.2 mm','3.6 mm','4.0 mm'});
    title('Bias at the Probed Points After Bias Removal')

    
    %%
    display('After ICP:')
    max(Ds*1000)
    RMSE(Ds*1000)
    display('Before ICP:')
    max(abs(displacementBias))
    RMSE(displacementBias)


    %%% save corrected data
    %save the new visual pcd
    fileName = strcat(destinationFolder,'originalPcd.txt');
    fileID = fopen(fileName,'w');
    fprintf(fileID,'%f %f %f %f %f %f %f %f %f %f\n',pcd.');
    fclose(fileID);
    
    %now change and save the probed points.
    newDisplacementBias = [];
    for i=1:1:size(tactilePoints,1)
       
        %% knn search cannot involve z..... otherwise way off... (old comment.. why??)
        [Idx,D] = knnsearch(pcd(:,1:3),tactilePoints(i,1:3),'K',1); 
        correspondencePt = pcd(Idx,1:3);
        %project the new corresspondence to the normal
        projectionDistance =  dot((correspondencePt-probedPoints(i,1:3)),probedPoints(i,7:9));
        projectedPt = probedPoints(i,1:3)+ projectionDistance*probedPoints(i,7:9);
        %use the new projected pt as the probed points
        %use the new correspondence's geometry info..
        probedPoints(i,1:3) = projectedPt;
        probedPoints(i,[4:6 10]) = pcd(Idx,[4:6 10]);
        tmp = displacementBias(i)+projectionDistance*1000;
        newDisplacementBias = [newDisplacementBias;tmp];
    end
    
    fileName = strcat(destinationFolder,'probePcd.txt');
    fileID = fopen(fileName,'w');
    fprintf(fileID,'%f %f %f %f %f %f %f %f %f %f\n',probedPoints.');
    fclose(fileID);
    %first change the displacement in force data
    %You should not center the displacements to zero...
    %it should still be based on the 
    for i=1:1:size(probedPoints,1)
         forceData = dlmread(strcat(sourceFolder,'point/','force_',num2str(i-1),'.txt'),' ');
         forceData = forceData(:,1:5); 
         fileName = strcat(destinationFolder,'point/','force_',num2str(i-1),'.txt');
         fileID = fopen(fileName,'w');
         forceData(:,5) = forceData(:,5)-repmat(newDisplacementBias(i)/1000,size(forceData,1),1);
         fprintf(fileID,'%f %f %f %f %f\n',forceData.');
         fclose(fileID);
    end
    
end
