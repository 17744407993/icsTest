# -*- coding:utf-8 -*-
import xlwt
import os


def increaseIP(ip):
	ip1 = int(ip.split('.')[-1])
	ip2 = int(ip.split('.')[-2])
	ip_pre2 = '%s.%s'%(ip.split('.')[0],ip.split('.')[1])
	for i in range(0,int(1)):
		# print("## ip1:%s##1" % (ip1))
		# print("## ip2:%s##2" % (ip2))
		#print("## ipNew:%s##" % (ipNew))
		ip1New = ip1 + 1
		if 2<=ip1+1<=254:
			ipNew = ip_pre2+'.'+str(ip2)+'.'+str(ip1New)
			#ip1 = ip1 + 1
			print("if3")
		else:
			ip2New = ip2+(ip1New%254)
			ip1New = ip1New%254+1
			print("aaaa## ip1:%s##4" % (ip1))
			print("aaaa## ip2:%s##5" % (ip2))
			print("aaaa## ip1New:%s##6" % (ip1New))
			print("aaaa## ip2New:%s##7" % (ip2New))
			ipNew = ip_pre2+'.'+str(ip2New)+'.'+str(ip1New)
			print("aaaa## ipNew:%s##8" % (ip1New))
			#ip1 = ip1 + 1
			print("else")
		print("---## ip1:%s##9" % (ip1))
		print("---## ip2:%s##10" % (ip2))
		print ("---## ipNew:%s##11"%(ipNew))

		return ipNew



def wrtChannelsExl(ip,devicesTotal,channelNumInt):
		new_workbook = xlwt.Workbook(encoding='utf-8')
		instructionssheet = new_workbook.add_sheet('使用说明')
		drivesheet = new_workbook.add_sheet('驱动')
		partitionsheet = new_workbook.add_sheet('分区')
		camerasheet = new_workbook.add_sheet('数字摄像机')
		encodersheet = new_workbook.add_sheet('编码器',cell_overwrite_ok=True)
		encodercamerasheet = new_workbook.add_sheet('编码器摄像机',cell_overwrite_ok=True)
		decodersheet = new_workbook.add_sheet('解码器')
		TVwallesheet = new_workbook.add_sheet('电视墙')
		usersheet = new_workbook.add_sheet('用户')
		encodertitle1 = ['编码器ip(必填，主键，唯一标识)','编码器ID(新增时无需填写，主键，唯一标识，规则：[当前节点id]-[Encoder]-[系统生成的编号])', '编码器名称(必填)','驱动id(必填)','端口(必填)','通道个数(必填)','用户(必填)','密码','设备参数','录像驱动ID','国标id','国标名称','密码','是否检测心跳','心跳间隔时间','心跳检测次数','是否鉴权','是否校时']
		encodertitle2 = ['ip','id','name','driverId','port','channelNum','username','password','deviceParam','recordDriverId','gbId','gbName','gbPassword','keepAlive','interval','times','auth','adjustTime']
		encodercameratitle1 = ['摄像机名称(必填)','摄像机ID(新增时无需填写，主键，唯一标识，规则：[当前节点id]-[Camera]-[系统生成的编号])','摄像机键盘编号(不能重复，建议填写，也用于排序)','类型(必填，1:球机,2:半球,3:固定枪机)','编码器ip(必填)','通道号(必填，小于所属编码器通道)','组播地址','组播端口','通道地址','通道参数','分区ID或编号','拾音器(1:有，0:无)','设备参数']
		encodercameratitle2 = ['name','id','mappingId','deviceSubType','encoderIp','channelNo','multicastIp','multicastPort','channelAddr','channelParam','zoneId','audio','deviceParam']
		##instructionstitle = ['协议']
		for i in range(0, len(encodertitle1)):
			encodersheet.write(0, i, encodertitle1[i])
		for j in range(0, len(encodertitle2)):
			encodersheet.write(1, j, encodertitle2[j])
		for k in range(0, len(encodercameratitle1)):
			encodercamerasheet.write(0, k, encodercameratitle1[k])
		for g in range(0, len(encodercameratitle2)):
			encodercamerasheet.write(1, g, encodercameratitle2[g])
		encNum = 2
		encodercamerasheetencNum = 2
		nameNum = 0
		for m in range(devicesTotal):
			data = [ip,"",ip,"Encoder-rtsphost-RTSP","554",channelNumInt,"admin","admin","","","","","","1","15","3","1","1"]
			for k in range(len(data)):
				encodersheet.write(encNum,k,data[k])
			print("==============a",encNum)
			encNum = encNum + 1
			for channel in range(channelNumInt):
				nameNum = nameNum+1;
				camerName = '摄像机名称_'+str(nameNum)
				data = [camerName,"","","1",ip,channel+1,"","null","","","","0",""]
				for k in range(len(data)):
					encodercamerasheet.write(encodercamerasheetencNum,k,data[k])
				print("==============",encodercamerasheetencNum)
				encodercamerasheetencNum = encodercamerasheetencNum + 1
			ip = increaseIP(ip)
		new_workbook.save('D://Program Files//pythonCode//first//test//testBook11.xls')

if __name__ == '__main__':

	ip = '1.1.1.1'
	devicesTotal = 3
	channelNumInt=10
	wrtChannelsExl(ip,devicesTotal,channelNumInt)
	print ("--Ready to exit… ")
