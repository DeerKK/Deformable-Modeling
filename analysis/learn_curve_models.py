# paper fig 3 (b)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 130
#from training_data import *

r2_mean_RF = [0.4026208983525963, 0.2878540305336771, 0.3770111757921569, 0.3255288116139533, 0.33947463597250516, 0.2393234737461643, 0.14959230213332844, 0.26578188244951756, -0.0171485301894318, -0.4012460749763994] \
+[0.4458740784708553, 0.47028612497490296, 0.5587968151991813, 0.7157165141106547, 0.7502230535222217]
r2_std_RF = [0.1974316116319137, 0.5966143950925393, 0.18655328746346025, 0.26942765330247553, 0.2887902180355897, 0.43242017031266355, 0.5472871463955827, 0.4883399630517717, 0.731761288964901, 0.9527043774143581]\
+[0.16126135485437207, 0.2028399524269655, 0.14308529186927804, 0.03805072005093706, 0.021863883060539897]
rmse_mean_RF = [0.5594491517861901, 0.5834872017209597, 0.5719300529645018, 0.5895592259868858, 0.5836595689938816, 0.6179639522276437, 0.6478944766196608, 0.605314101474598, 0.7014641204576807, 0.8203141926972205]\
+[0.5409438577089967, 0.5243593629944001, 0.48133722213640057, 0.3908185509864991, 0.3639891882896082]
rmse_std_RF = [0.09057482374041233, 0.21006157224682723, 0.09053686514914837, 0.12429648896082392, 0.1202086165693825, 0.1666940058687005, 0.19491967656834103, 0.168851736418656, 0.23449379309935575, 0.2842426035011251]\
+[0.07841068986818646, 0.10278322923792743, 0.08200727683315924, 0.025496908256488055, 0.01585041195213361] 

r2_mean_kNN = [0.5237062272707405, 0.4660997931818699, 0.4270551678147191, 0.3851098985048316, 0.4029051806815601, 0.3090021066398083, 0.081133891655543, 0.1649184542680041, -0.0421794208055834, -0.30853779419533517]\
+[0.4798435727506728, 0.5899215742006344, 0.6207381817275757, 0.6658018350099965, 0.6752350351320622]
r2_std_kNN = [0.08869481859105635, 0.23338542335231746, 0.214962068386058, 0.3045370505922696, 0.21924146691422833, 0.27270193774882345, 0.6734898615218963, 0.580974277943439, 0.8155731418064364, 0.8617288741944149] \
+[0.2417521823558464, 0.1017293794225362, 0.09354464572972183, 0.05959444663677612, 0.05452515249264055] 
rmse_mean_kNN = [0.5037931201210265, 0.5257424939896009, 0.5467032641118554, 0.5598057500278893, 0.5563049781342443, 0.5982201743079998, 0.665781180463626, 0.6401589272432278, 0.7039845233979467, 0.795886151831647] \
+[0.5178487344731366, 0.46560102754529636, 0.4490425941882177, 0.4230181515273239, 0.4140407109165527] 
rmse_std_kNN = [0.04713619072053134, 0.10670529100619731, 0.09848910693071383, 0.13123101792138223, 0.1084008211758648, 0.11933959189847503, 0.2265502249922848, 0.19883127867989936, 0.25492542696454484, 0.26531514743222173]\
+[0.1102561929141112, 0.06026840363518322, 0.05535478574630412, 0.03818539182450526, 0.03733116901014641]
  
r2_mean_GB = [0.5506650197060607, 0.36738345969127023, 0.4751353101063655, 0.45775787488506314, 0.44299123237827553, 0.16670111206626953, 0.0010700430768922956, 0.15634061435797572, -0.15776616306452085, -0.42103532746940325]\
+[0.5329249934164337, 0.6742814847800382, 0.71639267383517, 0.7920223495855807, 0.820411400887961]
r2_std_GB = [0.223790990549338, 0.5875231751995516, 0.23704816476189283, 0.246348989030707, 0.20551905796141345, 0.5543205654085015, 0.9694061267888764, 0.9501781662953197, 1.0265153314060635, 0.9843401683739602] \
+[0.15158777203743948, 0.10326781432778506, 0.06778762155832685, 0.0425658299366111, 0.026021684358163447] 
rmse_mean_GB = [0.47906019776603626, 0.5478289093400119, 0.5206022694300741, 0.5279555348304446, 0.5387211234746961, 0.6388844268249855, 0.6716093163822461, 0.6255820228774025, 0.7308097606745353, 0.8243674203985868]\
+[0.4958714934758845, 0.4129387150887275, 0.3884344700460042, 0.3332741015926823, 0.30815983457394464] 
rmse_std_GB = [0.10971216019135367, 0.20405377594944318, 0.10777316569399732, 0.11427373124759298, 0.09692108633401515, 0.2016896008305257, 0.29493286215925796, 0.25033125295206243, 0.2978195703877974, 0.2911826950860011]\
+[0.07627530484801698, 0.0678504419926826, 0.048337843396387574, 0.031294756918339064, 0.022893073940210205]
 
 
r2_mean_AB = [0.6121905258232542, 0.5446986928539395, 0.5661832754351668, 0.4658747798755518, 0.4671228289518118, 0.38207901353004936, 0.2558463662452682, 0.2604861066284647, 0.036899615480642814, -0.27067129572898846]\
+[0.5638410328696892, 0.6447686278700677, 0.6593396748717126, 0.7164786291459813, 0.7044487696701325]
r2_std_AB = [0.1006287899156923, 0.19034877981046724, 0.09966019165963527, 0.16719355482568718, 0.12932950443221913, 0.3088679322214679, 0.47856933863405693, 0.5141518993885998, 0.7167301103878233, 0.8544371417190644]\
+[0.19693173711767722, 0.08594146224598531, 0.059936032863852476, 0.023485584637606426, 0.031021287199495762]
rmse_mean_AB = [0.45332395457874264, 0.4866899247648666, 0.4797978345817995, 0.5291517825109777, 0.5309195389726745, 0.5622300071080424, 0.6053250458935749, 0.6029505270075519, 0.6804097114816684, 0.7830793186271007] \
+[0.475689618089176, 0.43323804879991423, 0.42727139491899696, 0.39084508103444976, 0.3958963724110549] 
rmse_std_AB = [0.05409364765640204, 0.09232574880631837, 0.05724687958183978, 0.08596631896161805, 0.06737334415594595, 0.12854101017801756, 0.18466664170081207, 0.18520988943688516, 0.23447271266647238, 0.26507800632117445]\
+[0.09337680829571866, 0.0557565379267936, 0.038770564143389294, 0.015389460412978074, 0.022391966629575384]  
 

r2_mean_ET = [0.6101379468363405, 0.6058490230740625, 0.6006341489349108, 0.5764955157414655, 0.5416491806578211, 0.45565908966290475, 0.26731602515172426, 0.37315762947815717, 0.0008298431587682767, -0.4609439418717342]\
+[0.6313884104917776, 0.6931966756543556, 0.7324143239634282, 0.8155656611193767, 0.8179534062499499]
r2_std_ET = [0.09891920563087873, 0.10711686196212226, 0.09287007956547295, 0.2007607123606704, 0.13423689678127804, 0.22588750588156134, 0.5946566550510949, 0.4828532212845361, 0.7856901566737757, 1.0117393709146105]\
+[0.07485138117856159, 0.0846166658332888, 0.07414157251297314, 0.01967794180300031, 0.01728026163972233]      
rmse_mean_ET = [0.45433619537005765, 0.4570400425107075, 0.46029985040667326, 0.466857003847994, 0.4915984093177881, 0.5304614584832623, 0.593971815547431, 0.556213794165918, 0.690763606707846, 0.8357276744702125] \
+[0.44343025125781893, 0.4021616708321877, 0.3768929791665092, 0.31517127250959803, 0.3108193940136203]
rmse_std_ET = [0.05616756496881432, 0.058420756684801435, 0.05512826299497681, 0.09867292231432714, 0.07008122539122641, 0.10804874738534975, 0.2038305811769611, 0.1667899098923778, 0.245601065742846, 0.2956269242856344]\
+[0.04589132249160404, 0.05654663289688554, 0.05265023689111099, 0.01731298089176829, 0.017176812896456315] 


r2_mean_ET_A = [0.7039974625739881, 0.6464312482365028, 0.628082067746105, 0.6408354935059786, 0.5529982079178955, 0.48332926406074844, 0.34827384578409176, 0.39953370796353826, 0.15344123946036248,-0.03507015683379262]\
+[0.6739297699889752, 0.7341460177683704, 0.7558666680195755, 0.8310597920841598, 0.8198738246148187]
#this is loc_cur: [0.6895659723312931, 0.7047925971854295, 0.7715724580790286, 0.8263269141244921, 0.8316118777317213]
r2_std_ET_A = [0.04860457316838236, 0.13411144488264307, 0.0974139282729136, 0.1118261422762463, 0.43784770718550764, 0.23131896825059348, 0.45474251381072583, 0.255781456346649, 0.5211999466064939,0.6222112012454832]\
+[0.04897681984490015, 0.05531134942107949, 0.06715525866063649, 0.02106197317626699, 0.01555532768590909]
rmse_mean_ET_A = [0.3974943368046349, 0.43027555833949044, 0.4437574402386295, 0.4346974853360313, 0.5167351266748368, 0.5147912241218947, 0.5643052897050983, 0.5560841047144331, 0.6477051611044382,0.5566785585304597]\
+[0.4180732912112929, 0.37559001063958736, 0.35991478966741336, 0.30129600666688383, 0.3069046820193081]
rmse_std_ET_A = [0.03336591894809099, 0.07345234019342563, 0.05701632423070228, 0.06485202313327525, 0.16337920666251057, 0.11498202249983912, 0.17988389843894367, 0.11689983702278665, 0.18890446454135318,0.3350391770654694]\
+[0.030642098365727562, 0.041666052794113985, 0.050090705628533495, 0.01737557252187638, 0.01296926222724342]


r2_mean_M = [-0.03212542,  0.34388554, 0.33563994,  0.37768577,  0.46857621,  0.52037001,0.41299038,  0.48904417 , 0.47955749 , 0.51018262 , 0.57995954,  0.60837003]
r2_std_M = [0.4853836,  0.29841071, 0.25913384, 0.2024174,  0.16160538, 0.11570027,0.19524336, 0.18545074, 0.17595344, 0.07572311, 0.03907769, 0.03166615]
rmse_mean_M = [0.72599887, 0.58241813, 0.71511648, 0.57122156, 0.52777651, 0.50418704,0.55438008 ,0.51646948, 0.52251918 ,0.5116349 , 0.48049491 ,0.45811489]
rmse_std_M = [0.16611057, 0.11480322 ,0.29068843,0.0901501,  0.08044799, 0.06132013,0.09074015, 0.09173807, 0.08889953 ,0.04012416 ,0.07644203 ,0.01840632]

#data transfer
r2_mean_RF = np.array(list(reversed(r2_mean_RF[0:10]))+r2_mean_RF[10:])
r2_std_RF = np.array(list(reversed(r2_std_RF[0:10]))+r2_std_RF[10:]) 

r2_mean_kNN = np.array(list(reversed(r2_mean_kNN[0:10]))+r2_mean_kNN[10:])
r2_std_kNN = np.array(list(reversed(r2_std_kNN[0:10]))+r2_std_kNN[10:]) 

r2_mean_AB = np.array(list(reversed(r2_mean_AB[0:10]))+r2_mean_AB[10:])
r2_std_AB = np.array(list(reversed(r2_std_AB[0:10]))+r2_std_AB[10:]) 

r2_mean_GB = np.array(list(reversed(r2_mean_GB[0:10]))+r2_mean_GB[10:])
r2_std_GB = np.array(list(reversed(r2_std_GB[0:10]))+r2_std_GB[10:]) 

r2_mean_ET = np.array(list(reversed(r2_mean_ET[0:10]))+r2_mean_ET[10:])
r2_std_ET = np.array(list(reversed(r2_std_ET[0:10]))+r2_std_ET[10:]) 

r2_mean_ET_A = np.array(list(reversed(r2_mean_ET_A[0:10]))+r2_mean_ET_A[10:])
r2_std_ET_A = np.array(list(reversed(r2_std_ET_A[0:10]))+r2_std_ET_A[10:])

r2_mean_M = np.array(r2_mean_M)
r2_std_M = np.array(r2_std_M)

rmse_mean_RF = np.array(list(reversed(rmse_mean_RF[0:10]))+rmse_mean_RF[10:])
rmse_std_RF = np.array(list(reversed(rmse_std_RF[0:10]))+rmse_std_RF[10:])

rmse_mean_kNN = np.array(list(reversed(rmse_mean_kNN[0:10]))+rmse_mean_kNN[10:])
rmse_std_kNN = np.array(list(reversed(rmse_std_kNN[0:10]))+rmse_std_kNN[10:])

rmse_mean_AB = np.array(list(reversed(rmse_mean_AB[0:10]))+rmse_mean_AB[10:])
rmse_std_AB = np.array(list(reversed(rmse_std_AB[0:10]))+rmse_std_AB[10:])

rmse_mean_GB = np.array(list(reversed(rmse_mean_GB[0:10]))+rmse_mean_GB[10:])
rmse_std_GB = np.array(list(reversed(rmse_std_GB[0:10]))+rmse_std_GB[10:])

rmse_mean_ET = np.array(list(reversed(rmse_mean_ET[0:10]))+rmse_mean_ET[10:])
rmse_std_ET = np.array(list(reversed(rmse_std_ET[0:10]))+rmse_std_ET[10:])

rmse_mean_ET_A = np.array(list(reversed(rmse_mean_ET_A[0:10]))+rmse_mean_ET_A[10:])
rmse_std_ET_A = np.array(list(reversed(rmse_std_ET_A[0:10]))+rmse_std_ET_A[10:])

rmse_mean_M = np.array(rmse_mean_M)
rmse_std_M = np.array(rmse_std_M)


#cat
r2_mean = [r2_mean_RF,r2_mean_kNN,r2_mean_AB,r2_mean_GB,r2_mean_ET,r2_mean_ET_A,r2_mean_M]
r2_std = [r2_std_RF,r2_std_kNN,r2_std_AB,r2_std_GB,r2_std_ET,r2_std_ET_A,r2_std_M]

rmse_mean = [rmse_mean_RF,rmse_mean_kNN,rmse_mean_AB,rmse_mean_GB,rmse_mean_ET,rmse_mean_ET_A,rmse_mean_M]
rmse_std = [rmse_std_RF,rmse_std_kNN,rmse_std_AB,rmse_std_GB,rmse_std_ET,rmse_std_ET_A,rmse_std_M]

#plot
param_range = [1,2,3,4,5,6,7,8,9,10,15,20,30,50,75]
param_range = [10,20,30,50,75]
param_range = [1,2,3,4,5,6,7,8,9,10,15,20]

color = plt.cm.BuPu(np.linspace(0, 1, 5)).tolist()+['C1','C3']
color = plt.cm.Pastel1(np.linspace(0, 1, 9)).tolist()[0:4]+plt.cm.tab10(np.linspace(0, 1, 10)).tolist()[0:3]
colors = ['b', 'g', 'r', 'c', 'y', 'm', 'k']
lable = ['RF','kNN','AB','GB','ET','Auto-ET','Auto-M']
marker = ['o','D','v','^','s','*','X']
para = 1
for i in range(7):
    tmp_mean = np.hstack((r2_mean[i][9],r2_mean[i][11:15]))
    tmp_std = np.hstack((r2_std[i][9],r2_std[i][11:15]))

    tmp_mean = r2_mean[i][:12]
    tmp_std = r2_std[i][:12]

    tmp_mean = rmse_mean[i][:12]
    tmp_std = rmse_std[i][:12]

    if i < 7:
        plt.plot(param_range, para*tmp_mean,  marker=marker[i], markersize=5, label=lable[i],color=colors[i])
        #plt.plot(param_range, tmp_mean+tmp_std, color=color[i], marker='o', ls=':',markersize=5, label=lable[i])
        #plt.plot(param_range, tmp_mean-tmp_std, color=color[i], marker='o',ls=':', markersize=5, label=lable[i])
        print(tmp_mean)
    else:
        plt.plot(param_range,para*tmp_mean,marker=marker[i],markersize=5,label=lable[i],color=colors[i])
    if i > 3:
        plt.fill_between(param_range,para*(tmp_mean+tmp_std),para*(tmp_mean-tmp_std),alpha=0.15,color=colors[i])

plt.xlabel('Number of pokes in the training set',fontsize=19)
plt.ylabel('RMSE (N)',fontsize=19)
plt.xticks([1,5,10,15,20],fontsize=16)
plt.yticks(fontsize=16)
#plt.legend(loc='upper right',fontsize=10)
ax = plt.subplot(111)
ax.legend(loc='upper right', ncol=2, fancybox=False, shadow=False,fontsize=14)

#plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
#plt.ylim([0,1])
plt.grid()

plt.show()