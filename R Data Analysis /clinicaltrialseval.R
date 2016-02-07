sponsors <- scan("Sponsors.txt", what = "", sep = "\n")
test <- head(sponsors)
test <- c()
testmatrix <- lapply(test, function(x) cbind(clinicaltrials_search(query = x), "Sponsor" = x));
df3 <- rbind.fill(testmatrix)

sapply(test, function(x) write.table(str(x)))


trials <- read.csv("trials.csv", header = FALSE)
colnames(trials) <- c("id", "sponsor", "published", "state", "url", "closed", "title", "condition", "intervention", "locations", "last_changed")
trials$published[trials$published=="False"] <- 0
trials$published[trials$published=="True"] <- 1
trials$published <- as.numeric(trials$published)
sponsors <- unique(trials$sponsor)
sponsor_reputation <- ddply(trials, .(sponsor), summarize, total_published = sum(published), total_trials = length(published))
sponsor_reputation <- sponsor_reputation[order(-sponsor_reputation$total_published),]
sponsor_reputation <- cbind(sponsor_reputation, "Rank" = 1:length(sponsors))
rownames(sponsor_reputation) <- sponsor_reputation$sponsor
sponsor_reputation <- sponsor_reputation[,-1]
head(sponsor_reputation, 10)
sponsor_of_trials <- trials$sponsor
sponsor_reputation["MedImmune LCC",] <- 5
sponsor_reputation["Eastern Cooperative Oncology Group",] <- 17
sponsor_reputation <- cbind("Sponsor" = rownames(sponsor_reputation), sponsor_reputation)
rank_of_trials <- sapply(sponsor_to_trials, function(x) sponsor_reputation[x,]$Rank)
trials2 <- cbind(trials, Rank = rank_of_trials)
trials2$published[trials$published==0] <- "False"
trials2$published[trials$published==1] <- "True"
trials2_published <- trials2[trials2$published=="True",]

nplotdata <- head(sponsor_reputation, 10)
temp1 <- cbind("Sponsor" = nplotdata$Sponsor, "Status" = "Published Trials", "Frequency" = as.numeric(nplotdata$total_published))
temp2 <- cbind("Sponsor" = nplotdata$Sponsor, "Status" = "Complete Trials", "Frequency" = as.numeric(nplotdata$total_trials))
nplotdata <- as.data.frame(rbind(temp1, temp2))
nplotdata$Sponsor <- as.factor(nplotdata$Sponsor)
nplotdata$Status <- as.factor(nplotdata$Status)
nplotdata$Frequency <- as.numeric(nplotdata$Frequency)
n1 <- nPlot(Frequency ~ Sponsor, group = "Status", data = nplotdata, 10, type = 'multiBarChart')
n1$xAxis(axisLabel = 'Sponsors Ordered In Descending Rank')
n1$yAxis(axisLabel = 'Frequency')
n1$chart(margin = list(left = 100))
n1$xAxis(rotateLabels=15)
n1$chart(reduceXTicks = FALSE)
n1$set(Title = "Top 10 Sponsors with The Most Published Data")
n1$chart(margin = list(bottom=125,left = 100))
#n1$addParams(height = 500, title = "Top 10 Sponsors with The Most Published Data")=
n1$save("graph1.html", 'inline', standalone=TRUE)



weighted_lambda_normalization <- function(total_published, total_trials, max, lambda) {
  lambda*total_published/total_trials-(1-lambda)*(max-total_published)/max
}
lambda_score <- weighted_lambda_normalization(sponsor_reputation$total_published, sponsor_reputation$total_trials, max(sponsor_reputation$total_trials), 0.9)
sponsor_reputation_scored <- cbind(sponsor_reputation, "Lambda" = lambda_score)
sponsor_reputation_scored <- sponsor_reputation[order(-sponsor_reputation_scored$Lambda),]
head(sponsor_reputation_scored,10)