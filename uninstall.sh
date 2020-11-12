python setup.py install --record files.txt
cat files.txt | xargs sudo rm -rf
python setup.py install
systemctl stop tacker
systemctl start tacker