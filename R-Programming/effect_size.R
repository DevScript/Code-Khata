install.packages("esc")

library(esc)

# Define the data we need to calculate SMD/d
mc <- 20.9   #control
sc <- 4.5  # control
nc <- 11  # control

mt <- 40.2   # biochar
st <- 10.1  # biochar
nt <- 5  # biochar

# Calculate effect size based on biochar
esc_mean_sd(grp1m = mc, grp2m = mt, 
            grp1sd = sc, grp2sd = st, 
            grp1n = nc, grp2n = nt)


# Calculate effect size based on control
esc_mean_sd(grp1m = mt, grp2m = mc, 
            grp1sd = st, grp2sd = sc, 
            grp1n = nt, grp2n = nc)


# Calculate effect size based on control combine
esc_mean_sd(grp1m = mt, grp2m = mc, 
            grp1sd = st, grp2sd = sc, 
            grp1n = nt, grp2n = nc,
            es.type = c("or"), study=NULL)



# meta analysis
library(readxl)
df <- read_excel()
View(df)
summary(df)

# Import Libraries
library(dmetar)
library(meta)
library(metafor)

# to verify if all the outputs are numeric Mc, Nc, Sc, Me, Se, Ne
str(df) # info
df$Mc <- as.numeric(df$Mc) # to change datatype of column
# Overall

es <- metacont(Ne,
               Me,
               Se,
               Nc,
               Mc,
               SC,
               data=df,
               studlab=paste(df$author),
               comb.fixed=FALSE,
               comb.random=TRUE,
               method.tau="HE",
               prediction=TRUE,
               sm="ROM",
               backtransf=FALSE,
               byvar=df$ni.type
               )
es

# with subset
es <- metacont(Ne,
               Me,
               Se,
               Nc,
               Mc,
               SC,
               data=df,
               subset=df$experiment_type %in% c("Pot"),
               studlab=paste(df$author),
               comb.fixed=FALSE,
               comb.random=TRUE,
               method.tau="HE",
               prediction=TRUE,
               sm="ROM",
               backtransf=FALSE,
               byvar=df$ni.type
)
es

# to convert it into text file
sink("es1.txt")
print(es1)
sink()