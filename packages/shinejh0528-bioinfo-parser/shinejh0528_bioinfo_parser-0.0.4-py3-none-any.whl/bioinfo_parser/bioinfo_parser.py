import sys
import os


class parser : 
	def __init__(self) : 
		self.meta_info = []
		self.header = []
		self.variants = []

	
	def read_vcf(self, sVcf_file) : 
		fVcf = open(sVcf_file, 'r')
		lsVcf = fVcf.read().split("\n")
		fVcf.close()
		if lsVcf[-1] == "" : 
			del lsVcf[-1]

		for i in range(0, len(lsVcf)) : 
			if "##" == lsVcf[i][:2] : 
				self.meta_info.append(lsVcf[i])
			elif "#" == lsVcf[i][0] and "##" != lsVcf[i][:2] : 
				self.header.append(lsVcf[i][1:].split("\t"))
			else : 
				self.variants.append(lsVcf[i].split("\t"))
	

	def read_fasta(self, sFasta_file) : 
		fFasta = open(sFasta_file, 'r')
		lsFasta = fFasta.read().split(">")
		fFasta.close()
		dicFasta = {}
		sHeader = ""
		for i in range(0, len(lsFasta)) :
			if lsFasta[i] == "" :
				continue
			lsFasta[i] = lsFasta[i].split("\n")
			dicFasta[lsFasta[i][0]] = "".join(lsFasta[i][1:])

		return dicFasta


	def reverse_complementary(self, sSeq) : 
		sSeq = sSeq.upper()
		dicRevcom = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
		return "".join([dicRevcom[sSeq[j]] if j in dicRevcom.keys() else sSeq[j] for j in range(len(sSeq) - 1, -1, -1)])
