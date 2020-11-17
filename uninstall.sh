echo "record all files"
python setup.py install --record files.txt
echo "rm all files"
cat files.txt | xargs sudo rm -rf
echo "start installing"
python setup.py install
echo "daemon-reload"
systemctl daemon-reload
echo "stop tacker service"
systemctl stop tacker
echo "start tacker service"
systemctl start tacker