FROM pritunl/archlinux
WORKDIR /usr/local/src/clickcount
EXPOSE 8080
RUN pacman -S --noconfirm maven tomcat8 jdk8-openjdk && \
    useradd -ru 57 tomcat8
COPY . /usr/local/src/clickcount
RUN mvn clean package && \
    cp target/*.war /var/lib/tomcat8/webapps/ && \
    rm -rf /usr/local/src/clickcount
CMD /usr/share/tomcat8/bin/catalina.sh run
