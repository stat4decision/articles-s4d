# récupération des données
data <- read.csv2("data.csv",fileEncoding="UTF-8-BOM")

# tri à plat
table(data$csp)

summary(data$csp)

install.packages("questionr",repos='http://cran.us.r-project.org')
library(questionr)

freq(data$csp)

# tri croisé
table(data$csp,data$ville)

install.packages("gmodels",repos='http://cran.us.r-project.org')
library(gmodels)

CrossTable(data$csp,data$ville)