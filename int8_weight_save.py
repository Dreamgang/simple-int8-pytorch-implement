from train_fp32 import VGG
import torch

'''
read every conv's scale and change conv weights to int8 type 
'''

conv1_param_0="552.7056234715656 952.8644686646186 373.4618747354427 728.5610960080737 458.03140215291523 484.48764954733616 758.6046132078764 576.5003641164983 328.02008172073704 416.5137379527181 408.3607685063129 470.3198918313868 565.6934474858749 558.6113258517343 507.731807751638 498.3011184788192 934.7043335831997 516.9250300241753 418.02196222334356 405.60845358032094 312.0988864327185 355.5702610856083 503.5315712420463 423.30938891907033 531.8559210727897 542.9308409943271 995.817635574703 878.5038029076669 1084.4023702367642 578.2682136500143 263.1219343645693 459.5992872317547 300.9606901212462 553.417233179324 371.22972755893716 592.3169251541564 699.0669507065289 398.95994581186477 590.1604896818823 650.8621008605637 676.4706296766265 432.0744024724307 548.1966372597507 349.77966377291233 304.2529139871598 697.0680934049451 349.82468708664493 419.8184428146134 579.8984254105623 673.9468112799636 372.30127289188556 443.91627098124115 629.6143094320265 486.6891661792823 378.9096660529654 846.4464935165024 391.10382043236416 525.184910894208 653.0315464437288 521.2432034869149 343.55668406158657 608.2136662689136 503.67523954463945 647.0962473420527"
conv2_param_0="645.8603677864663 441.0161434975722 634.8994701836978 612.2738985669207 604.8103329803367 627.7151077021475 742.4657290133715 571.7925043802765 665.6058298985038 691.5863331696635 613.9472187651118 678.3677395040086 752.5476575139708 602.4249125571866 647.6660275998153 684.7619889629183 644.8076022123792 676.3528486639278 612.758736645821 756.831445049255 587.4467667090425 642.2168945604933 658.9883682270029 655.6746076488473 661.462023790768 663.3484603432017 637.6267894015477 588.6211485550482 483.75374518081054 575.5602340862074 567.6680573253223 661.0379483717487 601.3303853454419 638.5735316760451 560.3438297440374 659.5981800197334 561.7556430968126 458.81714209916123 595.0528355304705 677.3795222942136 636.753440485123 689.8293479623636 472.79971543787263 478.2097167827381 602.6667454870666 636.383966529536 641.4202271936881 629.3905264561 544.389627169475 560.0290203865113 743.997786903957 615.7709311307217 672.2670129113717 617.2525974857904 706.2976325990494 626.4969546318132 624.6885913904088 551.860771544718 595.1437101387663 755.0846085927426 486.08189155937436 650.8631943580011 707.9523898720286 623.3153013103273"
conv3_param_0="581.2881759420618 751.4180056413488 816.1584998234637 958.6099599170694 772.2912689522412 1051.5167669029101 666.0502061921976 832.5960067398379 894.8400938556626 870.9203554997298 887.0563342768886 978.5051364246369 1080.6791373562014 1040.867713792286 923.7400551220608 665.3039530931998 744.3948903927512 739.6940390012372 850.0683996394591 972.586127554831 832.1038058763565 742.3310252634619 610.3521164211566 862.6580195991246 670.7773887282067 819.596018122453 783.3288736993079 942.4811268248574 870.7636607354492 970.4976271115416 523.5206570684074 971.1790737909496 947.38748673736 637.9741640256656 575.979386233872 970.038671223578 836.4453171648016 602.9112037170593 992.8845578888114 826.8608195878534 614.9864302630598 921.6447253495546 814.3136515982916 653.9024363446758 749.3735070693841 940.8629365503416 824.4431874672013 768.1910769938247 865.7181725507181 834.408377188886 828.9261688190367 993.3568242608268 814.701765357079 936.0949957598632 1040.4123217709662 648.5256167530155 666.7743474623331 784.8274392259673 707.832268808683 748.8199872162928 944.3451789046059 887.849004871029 824.1710063611289 865.3109541184942 811.4589648816648 888.5569321420749 814.9594666271435 726.0600777376382 922.6965948519124 890.1719402834174 916.7504836621893 805.2699469718472 818.0490994988999 824.5206332695606 870.8978399493493 725.2631102944111 553.642783385414 780.3779978165817 816.4161069556665 932.3299007912003 1001.0001665431491 853.878984950263 876.8716317224341 882.0158565332498 658.0611027979943 772.8611225495525 863.8546837581558 879.4051875958306 832.3518251124987 814.070121305901 804.5380658218671 693.234423034236 745.5806605211648 875.6185064928394 1159.28792557826 871.8824020089203 912.5434763103239 796.5171338329416 728.4227362110508 835.2061156016322 813.6045449759346 758.8662849018405 798.0453367936293 835.5494419017546 831.4609611194544 665.8384773916536 841.0876125679592 847.901128508545 997.6443415916048 744.1552519636522 829.9644955294158 935.8466607555115 697.0859386393157 743.2977321062871 802.6187706073734 642.0710237132685 818.365810948159 675.8662694757627 783.694636974978 798.1051967796083 639.6584911841579 720.5316951237277 891.3642605300897 762.293177171093 962.6319625646765 899.448861598236 993.8543408639094 708.8225577016481"
conv4_param_0="692.2475403713732 859.7004118334638 691.7527657690065 1036.4342391951375 821.533003254679 844.3930705843027 793.7095096035879 895.4651247919154 724.976299603794 888.4741219193227 885.6784976390776 783.4521491966808 769.5000637425969 695.1928367979626 659.6451471515526 836.8671452378605 850.9493903900759 963.391148308187 800.8867093783656 581.165338953221 906.0424184927857 844.7049778551548 703.0313974319486 798.4891567958223 776.9775936339593 864.8848971244906 809.929342649501 909.1160538159068 636.5380084743516 908.9447331531973 731.1796303928496 932.0346326349146 649.6490449857052 738.1704939347613 723.685780637974 853.8466490918064 781.9960628725579 865.5881339181497 891.320633924631 797.5789458809675 889.4796326080738 719.0484345507011 910.2536221583097 827.7351756571927 863.7213529093908 906.3345528636844 911.8418970978805 890.177239865632 940.294411836191 872.7602334330633 810.1537667739859 851.32661814049 800.5730021876013 907.5834474180783 852.6766799614782 803.3880544508967 705.3377296946221 664.6202107161303 879.6732218094473 837.9499418152158 663.866814517599 743.8194200271736 870.0725103835574 741.7263987502747 640.4274930030945 856.969855119562 827.978264421815 902.9961935225147 807.4819405240393 805.470481024937 766.2890073625668 713.5582206509797 801.5789375772334 749.8751922787759 754.1059024172495 869.6442373182451 905.4056176877149 750.1028829869263 838.6082270497271 797.4218624742421 696.26594553509 887.9896118823629 886.7038856173335 698.8778961631368 809.7020427462637 591.7643525751753 629.4900537356046 901.766848244021 986.9048867323135 810.2418766433568 932.8168490547142 934.695722848881 711.7950202226411 896.0661573819992 791.3653274432685 916.5635582019544 830.5791249748448 723.1559847875347 889.6340357163584 947.1953340534966 816.0111231780717 934.1658530682599 937.3208164040985 917.7925886329231 797.4474542679376 915.135055027875 633.7117708698833 899.0055072201438 690.9270600229519 840.0564748703839 719.0122198300589 926.5513124563853 843.4874448636621 847.5855081892676 922.8533532973164 716.8565435840112 844.2073077972652 612.0867981675946 686.5983562388077 892.2260146936078 836.785637507614 864.1312816952203 831.3791243388362 830.9134724801446 839.0568552140037 856.7369193912992 747.6802382659921 883.549352211246"
conv5_param_0="1151.1834386118846 986.3878160848503 801.5594876422543 996.4288615564553 1289.6209609529499 1220.7965545990328 876.8062292682731 941.463243409954 1171.8041530534283 1075.2459491523039 1169.2955516332813 1251.3951627882118 1316.3276114976456 1035.4714514209625 773.898074186589 929.4547346943004 1189.9597799890691 1150.210731605935 892.2068672545323 1024.9516710312887 991.6986421840204 1338.2477840853287 875.3051104054164 1188.8455092057204 953.9119728193886 1162.9772318297125 889.8144107570874 1164.9255156845127 818.836067262182 1263.486823214447 836.6135538878785 1061.5643601032466 1332.172038617367 1243.547602926533 998.4522944312448 1151.00488481444 1079.7274247568964 987.6021389561331 1013.6013897433525 1205.470047530267 1154.0930147846902 930.7198235800499 1140.66154476007 1115.6644531604104 966.3137836827841 1112.4779923453737 1104.4512027464245 1122.185604577842 962.6201114800809 1064.1095379774888 1235.2589100831103 1443.316856356723 881.4347946234584 918.4104189935856 1273.2821865703556 965.7789879000364 920.8192409887141 1233.4423445811692 1267.1132892022583 802.1661968365788 1117.6158677160556 1155.9411446696095 1062.3563750632202 1003.0069319870194 987.3313321402787 1130.9921853384162 1341.8303059271918 1054.1669236892712 1262.60437335514 1218.9523328833382 795.732713490032 794.1701267772285 893.4971855259092 891.2279881635643 1190.215029736084 1063.3249900393118 1311.2437997923782 983.3787623689263 1155.8758499126295 1216.0726525165785 1078.6063215241477 999.7270111163988 1003.366606669069 1256.0839970845523 1319.6262187205573 1070.8764621428384 1181.6235723402926 1071.2276947746825 1015.0585856680277 1303.6146147011975 940.3346644807824 954.7364913730295 1062.2573995910668 1222.728192638647 899.43044700275 981.8111506444513 945.5855825150406 1165.169659581129 1218.5243984011454 1137.770684524634 1087.1659089536379 1056.4387219544676 1107.6944198119024 876.4044664121892 938.6579733758424 858.8920044417808 1088.971441162365 1116.4320768248824 1271.407722822377 1155.1707761705475 1142.9012057498908 1052.7801911706586 964.6036231040138 1313.0874305629004 841.2446023722734 1004.5349057971441 1043.9018805254793 1107.604593059727 1061.9648842910588 1067.4848498094632 1137.6970232055291 937.605725155443 860.463168233025 925.9418990269209 1005.4533336479249 1163.0717414186054 979.9284438698663 1082.8082198550915 1209.5236756363843 1221.454313908569 1024.4496929683246 1121.822168135795 1095.3787102888984 1202.3388356895546 1115.2571392866619 1060.0639606145164 781.3932488919951 1143.3499023410577 1240.5605253225517 1154.2969937011449 982.7643985481126 1008.5827410367373 1208.2123157245392 1070.8885048203533 1180.3320131477521 924.3020637094975 1108.405918693909 960.6452818874704 890.2728291282585 1032.5932277921431 947.6676955236991 1066.3462509461935 1155.619680403541 1281.1570797138615 1201.3065837119061 1139.4541254717992 1067.8148629512473 1013.6030773823222 1174.9345112603985 846.3411731305065 1120.8424109769842 1158.981145671461 1154.3150504808152 750.0288188384199 1077.4311518730499 1106.9000881784796 1134.2926144834814 1214.1521966553646 1135.8817464682224 808.819600121966 921.34204195754 969.0982583164157 865.0367613124671 1113.9131456724444 827.9604078587416 674.5535079953202 1025.3031449588502 1276.9574332076402 1531.183565140006 1123.3299602430861 970.2451752567508 1045.844554600755 1043.7197113798206 1027.6397987964806 1179.3589732572843 1200.0571567244317 1416.673443445391 988.9064230338803 1153.0894890422464 1074.2058132448137 1328.6709733863618 1062.993901036649 980.654119682981 1050.187976524991 819.2998546897825 857.9315372136294 1255.341826273223 676.2386499198105 1089.9205009312086 1018.4259313297069 1047.9660832238324 940.7155752373167 1143.8865313297172 820.4821611035177 1044.2872018840928 1171.2101946154698 933.0499927088583 858.2957066915101 1243.137132002261 1023.8221273592056 1203.6271009886807 1182.53020824293 1111.4096860754394 1073.3755578332734 919.1532711600732 1014.0619619638676 1272.1253439999211 1183.7308921746746 984.114445508932 642.0815687029649 998.8165519814779 997.7225902218144 1095.8896326695199 840.6968455024462 1150.6387002957592 986.266707801491 797.8818698771576 1064.7352037601675 890.3711363835567 1209.3910043337041 991.6794874763434 832.2996410286509 1206.4836804634192 984.7607643323288 801.8512603707464 956.1468980403243 1287.7508454106828 1176.68700100144 1130.9434100067515 1186.3213678482937 736.4908227979637 1362.893148543439 966.0032803752925 1033.2644146545906 1119.1986316161103 887.9363239851372 1078.613010214445 1220.932614759519 900.3046423626978 992.9231925643992 1056.6592875468862 1176.8905135271991 844.4343158252882 1112.6124012802288 1009.1485607646431 1038.4581874044131"
conv6_param_0="1016.3437241489185 986.0850440825935 927.6440003291391 870.3201315912551 1042.974184117282 978.3972998758926 1263.5931298150176 925.1208530172929 1073.9173714380397 1113.276499033684 1195.779082628018 1121.7879119385723 1075.6415933855335 1083.3509249156232 915.3421404730407 1189.052585994619 1045.8595702034247 940.4915581901187 752.479288341162 845.8240296742136 1037.5919884037623 1125.7169001193433 1034.6045740702739 1089.0540960956873 1289.7689896754325 1026.3168072236456 1095.30698691118 1188.5318386411275 1000.009002729049 948.7314676607085 1027.5193746458901 1121.4459076815222 1083.5194351294151 1072.0377061093752 1069.2592870041315 1191.4109755056802 1127.9714214927485 1172.8055909417321 1022.414613858146 1027.967453182983 1202.1243928692804 1180.4527443940678 1044.448705711277 1058.101188845625 1163.5336388644291 1069.525971578112 1161.0893112275464 1085.1260436657894 1064.7709194034512 1016.3953573764705 1067.533920916953 1118.009433946795 1101.88703830225 1216.9984486272433 826.3911593051579 793.0063770256247 862.7247341649119 1125.855196579222 1149.3500137013198 981.0464949345518 1040.3779675349783 1164.6018205354667 1176.2839209686108 909.9918926531413 960.4413283773563 1012.680296008594 1025.2432028732899 1024.7243678557966 1077.90065329223 1131.2529420743645 890.1417245728423 976.8709332603445 1044.0050100525664 1106.2496762988592 1028.5764024445693 1193.7475549769947 1047.419560146069 1198.498285675072 1004.7678497893811 984.7784010328888 1047.5144379397993 1007.4370454812221 1052.2980772109715 1022.5654352977778 1008.2591549922271 1045.0594033941277 878.6273348068486 1096.5502769833533 1124.9994938520747 1079.7530045219937 1076.0405176740712 1042.4225902229819 1064.5551988090926 852.7526953609525 928.6539600933228 1112.0588538161373 1173.6121116822924 1022.9523524664422 1170.4449035406922 765.3358304463159 1025.1917766703416 1083.3682073677535 1156.4500380097606 1086.0383780909099 1038.5896057147847 691.3654075144187 1187.6034031392637 1020.4797859331355 1114.2437963767052 1043.3233776727293 1229.488554905223 1139.297162125582 1044.5088024920678 919.4498558927336 1097.3632329190466 934.5465977992365 639.4770727813019 1126.299164416412 932.891487275945 965.5759119287941 1065.4975909235702 1038.70979051831 953.8765278229189 933.0524442467049 1176.0187890884529 947.8732170571733 1040.2515558626997 1149.4590638615587 908.3348248390265 1102.2162886663 622.8863584440429 1007.1831040309183 1038.0141928172407 926.4976269087459 1277.474599761782 1052.9109671017586 974.9406339039649 900.3677002355498 1084.6187566652668 1166.856614307874 1046.8943100935364 993.8656986296897 1211.9365647799596 1201.0161748748 997.4772576269714 1161.6749462630867 1080.035283141227 937.4297892747172 1211.6931889735513 1048.3718203012381 1098.471231110094 1065.884892708044 1136.340173579744 948.3446721979558 964.0667922026521 1033.98934640419 944.5884138093382 895.0747541854763 965.9745949040426 895.6761098340164 785.8662642742576 1171.1575669243389 909.1305031627679 1122.850827804874 1238.212925402865 1102.839417060523 1045.8901160933542 816.9032291580702 1330.6396909068285 1055.9125657279676 1089.67677669499 1149.0167910471655 1189.7009861403212 820.5954438546418 1141.6043221383143 904.4431668998656 965.8346955360028 957.3518416903295 1055.8398351255598 971.8876327592241 1167.9603584257634 1098.747659634456 1175.6688714644722 1043.2254905236884 1181.7206453993272 843.4595640304594 1223.0624568904002 1033.9518401273717 1083.4747372841032 1013.9171966156863 1055.8107326104955 1050.9593425296725 1082.7470052660972 1113.7680883040264 1022.7409078388159 1163.7094277069136 1011.8065179337261 1174.171140975195 1091.3798282427804 1156.204122834447 1024.3033624830496 992.1412526985268 792.6317985864955 1226.8701321406313 964.9445808417165 959.4003943494292 992.1212724555986 994.8382129805054 961.5643626107068 669.1691257283242 1201.0094051401238 1076.5727865811546 1067.2276679953754 1162.3038098992315 1101.2672621487684 971.7560980281716 1088.2083805250002 1091.9261254528726 1149.667611118429 972.1773119768579 985.3527923004256 1003.2843995679774 1136.8974627712826 962.5932573498203 936.6034860868185 1030.042645942763 934.1830551753627 804.8732827980057 1014.1592192325551 1229.6380022035253 959.4327948782375 1223.775637981299 1130.2164061897554 1097.6150021526469 912.5836354550543 877.3351409503804 953.1680740433147 964.6927162795762 1018.9091099067714 1052.7493715397475 995.8599897151955 1000.2667347999596 1117.876063925508 963.9154528318126 1330.2371966148885 943.8791544184869 968.923965141216 1148.6693637969427 1125.6607733472736 1047.8786604731176 870.111949751156 944.3132662384097 990.8549217129549 868.1572624220178 1121.9688142108425 1273.2057210427354"
conv7_param_0="1027.8729220137484 799.8202059755101 687.4749574685239 889.6315284428521 1260.7170877032083 1135.683542498992 970.9320190148444 1241.1571537615164 885.1213723223959 960.6452818874704 1028.998133144553 1123.2463878745425 1053.0007277133764 917.2187233104664 858.7820067837407 782.6772100820951 739.7814226262474 783.2015345660564 907.0498818459029 675.7329472255493 890.186165620418 1030.9716641508774 1102.9493826728324 839.379133137924 841.1163329222901 1156.9731221218042 1108.9497743345808 865.0278937870585 1084.4055436484382 764.0778121986893 835.7273161043622 901.0568713519692 1027.7539304432835 904.2165198845236 1138.146733657068 620.3267636404078 1110.6915043720282 929.4311180729902 1146.4587217322467 914.5861966021725 673.4600678926108 785.7551224251426 1174.8459184883147 1284.2453755937006 900.4693913387083 1062.0434240466725 1092.3536027194175 1096.444122595843 888.6731147790206 1142.6915055312 1055.412026271542 1211.827485870077 1073.7751702147348 1102.7085002346685 926.9158940668883 959.734116571061 886.5382328080567 746.908432394422 962.3155626307714 1107.4993818511925 835.6977334311913 1129.1953074172213 1069.257341869501 947.9351017658001 1061.3087012033018 1107.5380961000944 828.6041325276501 893.2171985398435 1149.8400880118525 955.737635627416 982.3926155945769 959.6426953010775 914.4830584337974 687.2027878281908 1112.1155188435537 955.359350248199 924.9678406752371 1094.6178235115822 939.3500869437368 821.2424022202424 713.5221386846495 878.2964850727766 840.1036738505559 1082.2830999619296 923.5676825974423 1158.3150185211196 827.9792296633826 892.8967867525477 838.8902767548033 1017.5601336549524 1084.0629914148926 798.1128947827277 1111.6673627066648 729.480385708979 921.4590865097275 680.6405457630118 1308.1780417142809 1010.8679394951796 1031.4696944061807 1079.2737563641952 936.5090089327842 1171.93474845205 1189.2818892930766 917.4826517093376 766.7841467937187 963.9141446294362 918.1610900948506 1107.7471134363777 1240.873175596681 671.3156186824112 1075.1453034408319 885.537701424204 1093.1649025452998 868.3737113459833 1145.9142076838864 788.4084773914182 1163.2322286472984 920.3641152812291 1053.6606124757798 1047.1809611899896 868.0842231047535 1126.0069900265157 1002.4925473747109 797.8451214559852 914.8388901745818 736.4663210339877 1098.246806089177 1174.7243883517278 886.6599760597952 921.7077180513816 966.0783962067924 1115.2210939295624 839.7280506333952 905.1022588938496 882.9387354583554 904.8305144432397 862.4910164709502 774.296652804205 983.5114196630836 954.0317793218815 948.6076038859537 1060.6386110838193 770.493180684029 1024.7939221491797 749.3862238664565 1136.0676018699444 1054.048023919452 991.8173948056241 869.3484922467483 750.0946969253586 921.9423219878274 930.1214615264737 982.1045131292761 873.5937168026575 908.6794929245119 1025.0422137082926 738.779837026499 740.589397824119 903.49310403242 1232.1951323465787 946.4625008065029 1057.5212794991096 945.075888495398 1034.958239012239 734.3463316354477 900.3515307081294 742.2506013981385 1034.2286227137413 885.2223147889159 1049.3191601556885 1263.1010852028232 736.8563789741172 968.5477189683659 1115.1021753703133 1016.6893182393892 762.0407882110961 969.3749204397956 865.5715192202852 1037.9379026917277 1077.4786216689515 1061.7268216826167 1071.3957541288173 822.481676464818 963.6582413346719 731.5669327045088 1123.0778745181558 915.3546255996297 972.5465067715634 943.1115736088018 1030.9270813740218 925.4792847157386 970.4586183110373 775.7954275832545 1048.278785622359 1134.5245389710092 1005.6349662757908 1049.4142532036078 944.9931059441759 1088.055493879802 925.5708458443974 924.5121157712864 870.9191095495172 1097.4786098680577 1099.1713522979412 1044.482049290438 790.1625237062875 1156.4862869850297 992.5836804865681 1121.9383151677762 1211.3329138659735 883.295062442351 1062.3672336958416 1135.9687994718163 1045.477512328435 1117.061797140549 871.8948892492845 923.8692265258111 665.3770850157421 1059.8048725410297 932.8852584587212 1018.9345081786021 901.3835487105551 830.2406790597778 671.640495793197 912.6662121982159 685.1449552146562 927.1468029860329 1029.6318755805237 1284.8855486240302 1233.0765147362745 996.1547067022374 1173.2188064088818 888.1182322845029 994.0476900719162 681.2059428461083 1144.4436417792642 873.6418940098902 1022.624941963978 721.0885815746128 1146.401509950479 960.6601162802363 957.9327884517902 1071.7122878419282 1090.5064283360896 883.1434007384237 1026.8536488568234 1139.1810477458678 984.4556925238169 949.3679804593061 811.9578242019634 1176.467643786528 714.7051839952744 872.3351145450705 869.7865930926939 1113.0051398042963 978.0350982123155"


conv1_param_0=conv1_param_0.split(" ")
conv2_param_0=conv2_param_0.split(" ")
conv3_param_0=conv3_param_0.split(" ")
conv4_param_0=conv4_param_0.split(" ")
conv5_param_0=conv5_param_0.split(" ")
conv6_param_0=conv6_param_0.split(" ")
conv7_param_0=conv7_param_0.split(" ")



model=VGG()
map=torch.load("./checkpoint/ckpt.pth")
model.load_state_dict(map['net'])


d_map={}
for name,i in model.named_parameters():
   print(name,i.shape)
   if name == "conv1.weight":
      for index, scale in enumerate(conv1_param_0):
          i[index, :, :, :] *= float(scale)
      i=torch.round(i)
      #i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv2.weight":
       for index, scale in enumerate(conv2_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv3.weight":
       for index, scale in enumerate(conv3_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv4.weight":
       for index, scale in enumerate(conv4_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv5.weight":
       for index, scale in enumerate(conv5_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv6.weight":
       for index, scale in enumerate(conv6_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)

   if name == "conv7.weight":
       for index, scale in enumerate(conv7_param_0):
           i[index, :, :, :] *= float(scale)
       i = torch.round(i)
       # i=torch.Tensor(i,dtype=torch.int8)


   d_map[name]=i
   torch.save(d_map,"./checkpoint/int8.pth")


'''
test part

model=VGG()
model.load_state_dict(torch.load("./checkpoint/int8.pth"))
for name,i in model.named_parameters():
   if name == "conv1.weight":
      print(i)
'''