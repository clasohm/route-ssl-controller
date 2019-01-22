FROM rhel7
MAINTAINER Carsten Clasohm <clasohm@redhat.com>

RUN yum -y install git https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum -y install python2-pip && yum remove -y epel-release && yum clean all && rm -rf /var/cache/yum
RUN pip install git+git://github.com/kubernetes-client/python.git

ADD controller.py /tmp

ENTRYPOINT  ["python", "-u", "/tmp/controller.py"]
