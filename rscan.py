# -*- coding: utf-8 -*- 

# # # # # # # # Thread Func # # # # # # # # 

import threading

CallBackEcho = None #callback func


def thread_proc(runner):
	runner.run()

def open_threads(runner,thread_num):
	runner.still_run = True
	thread_list = []
	try:
		for i in range(thread_num):
			t = threading.Thread(target=thread_proc,args=(runner,))
			t.setDaemon(True)
			t.start()
			thread_list.append(t)
	except:
		pass

	while True:
		try:
			alive = False
			for t in thread_list:
				alive = alive or t.isAlive()
         		if not alive:
             			break
		except KeyboardInterrupt:
			if runner.still_run:
				runner.still_run = False
				sys.stdout.write ('\nAccept Ctrl+C, Quitting...\n')
				sys.stdout.flush()
		except:
			break
	if CallBackEcho != None:
		CallBackEcho("end")

	runner.still_run = False

#multi-threads runner

class runner:
	still_run = False
	instance = 0

	#args: start instance in multi-threads
	def __init__(self,instance):
		self.instance = instance
		self.still_run = False

	def run(self):
		while self.still_run:
			if not self.instance():
				break

# # # # # # Socket Function # # # # # # # # 

import socket
import struct

# ip value to ip str
def ipint2str(ipvalue):
	return socket.inet_ntoa(struct.pack("!I",ipvalue))

# ip str to ip value
def ipstr2int(ip):
    return struct.unpack('!I', socket.inet_aton(socket.gethostbyname(ip)))[0]

# # # # # # # # # # # # # # # # # # # # # # # # 

#portchecker: check ports
import sys

class portchecker:
	timeout = 0
	ipport_iter = 0
	result = []

	data_mutex = 0
	iter_mutex = 0
	scanned_portnum = 0
	open_portnum = 0

	def __init__(self,ipport_iter,timeout = 5):
		self.ipport_iter = ipport_iter
		self.timeout = timeout
		self.data_mutex = threading.Lock()
		self.iter_mutex = threading.Lock()
		self.result = []

	def find_a_port(self,ip,port,result):
		clean_str = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
		clean_str += clean_str
		if CallBackEcho != None:
			CallBackEcho(result)
		sys.stdout.write ('%s%s                             \n' % (clean_str,result))
		sys.stdout.write ('%sOpen:%d,Scanned:%d                 ' % (clean_str,self.open_portnum,self.scanned_portnum))
		sys.stdout.flush()
		
	def on_scanning(self,ip,port):
		clean_str = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
		clean_str += clean_str
		sys.stdout.write ('%sOpen:%d,Scanned:%d                 ' % (clean_str,self.open_portnum,self.scanned_portnum))
		sys.stdout.flush()

	def connect(self,ip,port):
		s = socket.socket()
		s.settimeout(self.timeout)
		result = ''
		try:
			s.connect((ip,port))
			result = ('%s:%d' % (ip,port))
		except:
			pass
		s.close()
		return result

	def save_result(self,ip,port,report): 
		self.result.append(report)

	def __call__(self):
		# get ip:port from iterator			
		ip = 0
		port = 0
		try:
			self.iter_mutex.acquire()
			ip,port = self.ipport_iter.next()
		except:
			return False
		finally:	
			self.iter_mutex.release()

		self.data_mutex.acquire()
		self.on_scanning(ip,port)
		self.data_mutex.release()

		# link ip:port,get link report
		report = self.connect(ip,port)

		self.data_mutex.acquire()
		self.scanned_portnum += 1
		if report :
			self.open_portnum += 1
			self.find_a_port(ip,port,report)
			self.save_result(ip,port,report)
		self.data_mutex.release()
		return True


# # # # # # # # # # iterator # # # # # # # # # #

#iterlist_iter:  iterate in list of iterator

class iterlist_iter:
	current = 0
	iterlist_iter = 0
	def __init__(self,iterator_list):
		self.iterlist_iter = iter(iterator_list)
		self.current = self.iterlist_iter.next()
	def __self__(self):
		return self
	def next(self):
		try:
			return self.current.next()
		except:
			self.current = self.iterlist_iter.next()
		return self.current.next()

'''
list iterator
list of range
range_iter([[1,5],[6,9]]) -> 1 2 3 4 5 6 7 8 9
'''
class range_iter:
	list = 0
	range_iter = 0
	current = 0
	end = 0
	step = 1

	def __init__(self,list):
		self.list = list
		self.reset()

	def __iter__(self):
		return self

	def reset(self):
		self.range_iter = iter(self.list)
		self.current,self.end = self.range_iter.next()

	def next(self):
		if self.current<=self.end:
			current = self.current
			self.current = self.current + self.step
			return current
		else:
			self.current,self.end = self.range_iter.next()
			return self.next()

'''
IP+Port Iterator
Return (ip,port)
'''
class ipport_iter:
	current_ip = 0
	ip_iter = 0
	port_iter = 0

	def __init__(self,ip_iter,port_iter):
		self.ip_iter = ip_iter
		self.port_iter = port_iter
		self.reset()

	def __iter__(self):
		return self

	def reset(self):
		self.ip_iter.reset()
		self.port_iter.reset()
		self.current_ip = self.ip_iter.next()

	def next(self):
		try:
			ret = (ipint2str(self.current_ip),self.port_iter.next())
		except:
			self.current_ip = self.ip_iter.next()
			self.port_iter.reset()
			ret =  (ipint2str(self.current_ip),self.port_iter.next())
		return ret

'''

#range list
#example:

#ip
ips =	
	[
		[ipstr2int('192.168.0.0'),ipstr2int('192.168.0.255') ]
	]

#port 
ports = 
	[
		[80,80]
	]


'''

def ipport_iter_factory(ips,ports):
	ip_iter = range_iter(ips)
	port_iter = range_iter(ports)
	return ipport_iter(ip_iter,port_iter)

# # # # # # # # # # # # # # # # # # # # # # 

# use func

import string

s_ips = []
s_ports = []
s_addrlist = []

def hostlist_isnull():
	global s_ips,s_ports,s_addrlist
	return (len(s_ips)==0 or len(s_ports)==0) and len(s_addrlist)==0 

def host_iterator():
	global s_ips,s_ports,s_addrlist
	if hostlist_isnull():
		return False
	iter1 = 0
	try:
		iter1 = ipport_iter_factory(s_ips,s_ports)
	except:
		pass
	iter2 = iter(s_addrlist)
	iterlist = []
	if iter1:
		iterlist.append(iter1)
	if iter2:
		iterlist.append(iter2)
	return iterlist_iter(iterlist)

def addip(ipstart_str,ipend_str=''):
	global s_ips
	ipstart = ipstr2int(ipstart_str)
	if ipend_str:
		ipend = ipstr2int(ipend_str)
	else:
		ipend = ipstart
	item = [ipstart,ipend]
	s_ips.append(item)

def readiplist(listfile):
	print 'File',listfile,
	try:
		f = open(listfile,'r')
		print 'Read Success',
	except:
		print 'Read Failed'
		return False
	total = 0
	for line in f.readlines():
		if line[-1] == '\n':
			line = line[0:-1]		
		ip1 = 0
		ip2 = 0
		ips_iter = iter(line.split(' '))
		try:
			ip1 = ips_iter.next()
			ip2 = ips_iter.next()
		except:
			ip2 = ip1

		if ip2:
			total += 1
			addip(ip1,ip2)
		else:
			break
	print 'Add',total,'ip range'
	return total

def addport(portstart,portend=0):
	global s_ports
	if portend==0:
		portend = portstart
	item = [portstart,portend]
	s_ports.append(item)

def readportlist(listfile):
	print 'File',listfile,
	try:
		f = open(listfile,'r')
		print 'Read Success',
	except:
		print 'Read Failed'
		return False
	total = 0
	for line in f.readlines():
		if line[-1] == '\n':
			line = line[0:-1]
		port1 = 0
		port2 = 0
		ports_iter = iter(line.split(' '))
		try:
			port1 = ports_iter.next()
			port2 = ports_iter.next()
		except:
			port2 = port1

		if port2:
			total += 1
			port1 = string.atoi(port1)
			port2 = string.atoi(port2)
			addport(port1,port2)
		else:
			break
	print 'Add',total,'port range'
	return total

def addaddr(ip,port):
	global s_addrlist
	item = [ip,port]
	s_addrlist.append(item)

def readaddrlist(listfile):
	print 'File',listfile,
	try:
		f = open(listfile,'r')
		print 'Read Success',
	except:
		print 'Read Failed'
		return False
	total = 0
	for line in f.readlines():
		if line[-1] == '\n':
			line = line[0:-1]
		ip = 0
		port = 0
		addr_iter = iter(line.split(':'))
		try:
			ip = addr_iter.next()
			port = addr_iter.next()
		except:
			break

		total += 1
		port = string.atoi(port)
		addaddr(ip,port)
	print 'Add',total,'addr'
	return total

def addresult():
	global s_addrlist,s_result
	s_addrlist.extend(s_result)

def cleanip():
	global s_ips
	s_ips = []

def cleanport():
	global s_ports
	s_ports = []

def cleanaddr():
	global s_addrlist
	s_addrlist = []

def host():
	global s_ips,s_ports,s_addrlist
	print '\nHosts:'
	print ' ips:'
	for ip1,ip2 in s_ips:
		print '   [\'%s\',\'%s\']' % ( ipint2str(ip1),ipint2str(ip2) )
	print ' ports:'
	for port1,port2 in s_ports:
		print '   [\'%s\',\'%s\']' % ( port1,port2 )
	print ' addrs:'
	for ip,port in s_addrlist:
		print '   [\'%s\':%d]' % ( ip,port )
	print ''

s_timeout = 5
s_thread = 100
s_result = []

def settimeout(value):
	global s_timeout
	s_timeout = value

def setthread(value):
	global s_thread
	s_thread = value

def status():
	print 'Status:'
	print ' Timeout:',s_timeout
	print ' Thread:',s_thread
	print ''

def save(path):
	global s_result
	try:
		print 'File',path,
		output = open(path,'a')
		for s in s_result:
			output.write(s+'\n')
		print 'Save Success'
	except:
		print 'Save Failed'

import time
def rscanner(conn):
	global s_thread,s_result
	r = runner(conn)
	t =  time.clock()
	open_threads(r,s_thread)
	s_result = conn.result
	t = time.clock() - t
	if CallBackEcho != None:
		CallBackEcho('Total Time: %.4lfs'%(t))
	sys.stdout.write( '\nTotal Time: %.4lfs\n'%(t) )


def scan():
	global s_timeout
	host_iter = host_iterator()
	if not host_iter:
		print 'Host list Empty, Please check'
		return
	conn = portchecker(host_iter,s_timeout)
	rscanner(conn)

class data_sender:
	data = 0
	timeout = 0
	host_iter = 0
	iter_mutex = 0

	def __init__(self,data,timeout = 5):
		self.data = data
		self.timeout = timeout
		self.host_iter = host_iterator()
		self.iter_mutex = threading.Lock()

	def senddata(self,ip,port):
		s = socket.socket()
		s.settimeout(self.timeout)
		result = False
		try:
			s.connect((ip,port))
			s.send(self.data)
			result = True
		except:
			pass
		s.close()
		return result

	def __call__(self):
		ip = 0
		port = 0
		self.iter_mutex.acquire()
		try:
			ip,port = self.host_iter.next()
		except:
			self.host_iter = host_iterator()
			ip,port = self.host_iter.next()
		self.iter_mutex.release()
		if self.senddata(ip,port):
			sys.stdout.write('#')
		else:
			sys.stdout.write('!')
		sys.stdout.flush()
		return True

import os
def loadfile(filepath):
	data = 0
	try:
		f = open(filepath,'r')
		len = os.path.getsize(filepath)
		data = f.read(len)
	except:
		pass
	return data

def loadport(port):
	data = 0
	try:
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(('0.0.0.0',port))
		s.listen(1)
		ac,addr = s.accept()
		recvlen = 8192
		data = ''
		while True:
			buf = ac.recv(8192)
			data += buf
			if len(buf)!=recvlen:
				break
		s.close()
		ac.close()
	except:
		pass
	return data

def senddata(data):
	if hostlist_isnull():
		print 'Host list Empty, Please check'
		return
	if len(data)==0:
		print 'Data is Empty, Please check'
		return
	global s_timeout,s_thread
	ds = data_sender(data,s_timeout)
	r = runner(ds)
	open_threads(r,s_thread)

def help():
	print '-------Rattlesnake 1.2 By Chaser---------'
	print 'I\'m a Port Scanner in Python (PC or Android)\n'
	print 'usage: python -i me.py\n'
	print 'hosts:'
	print '	addip(ip,[endip]): add ip range'
	print '	addport(port,[endport]): add port range'
	print '	addaddr(ip,port): add addr (ip,port)'
	print '	addresult(): add scan result to addr list\n'
	print '	readiplist(listfile): read ip list from file'
	print '	readportlist(listfile): read port list from file'
	print '	readaddrlist(listfile): read addr list from file\n'
	print '	cleanip(): clean ip range list'
	print '	cleanport(): clean port range list'
	print '	cleanaddr(): clean addr list\n'
	print '	host(): watch the hosts you set\n'
	print 'settings:'
	print '	setthread(value): set thread num'
	print '	settimeout(value): set timeout value\n'
	print '	status(): watch the setting value you set\n'
	print 'actions:'
	print '	scan(): scanning hosts\n'
	print '	data = loadfile(filepath): load file,get data'
	print '	data = loadport(portnum): listen on port,get data'
	print '	senddata(data): send data to hosts\n'
	print '	save(filepath): save scan result to file\n'
	print 'others:'
	print '	help(): call this page\n'

if __name__ == '__main__':
	help()
