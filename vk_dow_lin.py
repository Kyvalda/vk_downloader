import re
import urllib2
f = open('source.htm')
urls=[]
for i in f:
    temp=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
    if len(temp)!=0 and '.mp3' in temp[0]:
        urls.append(temp[0])
print len(urls)
f.close()
for i in urls:
    if 'mp3' in i:
        print(i.split(',')[0])
        response = urllib2.urlopen(i.split(',')[0])
        mp3_name=i.split(',')[0].split('/')[-1]
        f = open('/mnt/flash/Music/from_VK/'+mp3_name, 'wb')
        meta = response.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (mp3_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = response.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status

        f.close()

