library(tidyverse)

# Read the data
df <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/all_naca_cl_vs_cd.csv")

setwd("C:/Pyhton/PyCharm Community Edition 2024.2.1/Files/WEbScraping/Personal Projects/airfoils/legacy")

# Create images directory if it doesn't exist
dir.create("images", showWarnings = FALSE)

# Remove invalid entries
df_clean <- df

# Plot Cl vs Cd for NACA 0009
ggplot(df_clean, aes(x = AOA_0009, y = Cl_NACA_0009)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for Airfoil NACA 0009",
       x = "AOA",
       y = "Cl (Lift Coefficient)") +
  theme_minimal()
ggsave("images/cl_vs_aoa_0009.png", width = 10, height = 6, dpi = 300)

ggplot(df_clean, aes(x = AOA_0012, y = Cl_NACA_0012)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for Airfoil NACA 0012",
       x = "AOA",
       y = "Cl (Lift Coefficient)") +
  theme_minimal()
ggsave("images/cl_vs_aoa_0012.png", width = 10, height = 6, dpi = 300)

ggplot(df_clean, aes(x = AOA_2412, y = Cl_NACA_2412)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for Airfoil NACA 2412",
       x = "AOA",
       y = "Cl (Lift Coefficient)") +
  theme_minimal()
ggsave("images/cl_vs_aoa_2412.png", width = 10, height = 6, dpi = 300)

# Plot Cl/Cd vs AOA for multiple airfoils
ggplot() +
  geom_line(data = df_clean, aes(x = AOA_0009, y = cl_vs_cd_0009, color = "NACA 0009")) +
  geom_point(data = df_clean, aes(x = AOA_0009, y = cl_vs_cd_0009, color = "NACA 0009")) +
  
  geom_line(data = df_clean, aes(x = AOA_0012, y = cl_vs_cd_0012, color = "NACA 0012")) +
  geom_point(data = df_clean, aes(x = AOA_0012, y = cl_vs_cd_0012, color = "NACA 0012")) +
  
  geom_line(data = df_clean, aes(x = AOA_2412, y = cl_vs_cd_2412, color = "NACA 2412")) +
  geom_point(data = df_clean, aes(x = AOA_2412, y = cl_vs_cd_2412, color = "NACA 2412")) +
  
  labs(title = "Cl/Cd vs AOA (Pre-Stall Only)",
       x = "AOA (Angle of Attack)",
       y = "Cl/Cd (Lift-to-Drag Ratio)",
       color = "Airfoil") +
  xlim(0, 12) +
  theme_minimal()
ggsave("images/cl_cd_comparison.png", width = 10, height = 6, dpi = 300)


#making Cl Vs AOA

df1 <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/all_naca_cl_vs_aoa.csv")

max_0009 <- df1[which.max(df1$cl_0009), ]
max_0012 <- df1[which.max(df1$cl_0012), ]
max_2412 <- df1[which.max(df1$cl_2412), ]

ggplot() + 
  geom_line(data = df1, aes(x = AOA, y = cl_0009, color = "NACA 0009")) +
  geom_point(data = df1, aes(x = AOA, y = cl_0009, color = "NACA 0009")) +
  geom_point(data = max_0009, aes(x = AOA, y = cl_0009), 
             color = "black", shape = 8, size = 3) +

  geom_line(data = df1, aes(x = AOA, y = cl_0012, color = "NACA 0012")) +
  geom_point(data = df1, aes(x = AOA, y = cl_0012, color = "NACA 0012")) +
  geom_point(data = max_0012, aes(x = AOA, y = cl_0012), 
             color = "black", shape = 8, size = 3) +
  
  geom_line(data = df1, aes(x = AOA, y = cl_2412, color = "NACA 2412")) +
  geom_point(data = df1, aes(x = AOA, y = cl_2412, color = "NACA 2412")) +
  geom_point(data = max_2412, aes(x = AOA, y = cl_2412),
             color = "black", shape = 8, size = 3) +
  
  labs(title = "Lift Coefficient (Cl) vs AOA",
       x = "Angle of Attack (degrees)",
       y = "Lift Coefficient (Cl)",
       color = "Airfoil") +
  theme_minimal()
ggsave("images/cl_vs_aoa_combined.png", width = 10, height = 6, dpi = 300)

df2 <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/0009_var_reynolds.csv")

ggplot() +
  geom_line(data = df2 %>% filter(AOA <= 8), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  geom_point(data = df2 %>% filter(AOA <=8), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  
  geom_line(data = df2 %>% filter(AOA <= 8), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  geom_point(data = df2 %>% filter(AOA <= 8), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  
  geom_line(data = df2 %>% filter(AOA <= 9), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  geom_point(data = df2%>% filter(AOA <= 9), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  labs(title = "Cl/Cd of NACA 0009 at Varying Reynold's number", 
       x = "AOA", 
       y = "Cl/Cd") +
  theme_minimal()
ggsave("images/reynolds_variation_0009.png", width = 10, height = 6, dpi = 300)

df3 <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/0012_var_reynolds.csv")

ggplot() +
  geom_line(data = df3 %>% filter(AOA <= 10), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  geom_point(data = df3 %>% filter(AOA <=10), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  
  geom_line(data = df3 %>% filter(AOA <= 10), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  geom_point(data = df3 %>% filter(AOA <= 10), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  
  geom_line(data = df3 %>% filter(AOA <= 12 & AOA != 11), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  geom_point(data = df3 %>% filter(AOA <= 12 & AOA != 11), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  labs(title = "Cl/Cd of NACA 0012 at Varying Reynold's number", 
       x = "AOA", 
       y = "Cl/Cd") +
  theme_minimal()
ggsave("images/reynolds_variation_0012.png", width = 10, height = 6, dpi = 300)

df4 <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/2412_var_reynolds.csv")

ggplot() +
  geom_line(data = df4 %>% filter(AOA <= 11), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  geom_point(data = df4 %>% filter(AOA <=11), aes(x = AOA, y = cl_cd_50, color = "50,000")) +
  
  geom_line(data = df4 %>% filter(AOA <= 12), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  geom_point(data = df4 %>% filter(AOA <= 12), aes(x = AOA, y = cl_cd_100, color = "100,000")) +
  
  geom_line(data = df4 %>% filter(AOA <= 13), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  geom_point(data = df4 %>% filter(AOA <= 13), aes(x = AOA, y = cl_cd_200, color = "200,000")) +
  labs(title = "Cl/Cd of NACA 2412 at Varying Reynold's number", 
       x = "AOA", 
       y = "Cl/Cd") +
  theme_minimal()
ggsave("images/reynolds_variation_2412.png", width = 10, height = 6, dpi = 300)

df5 <- read.csv("C:/Users/Dhruv/Documents/CLG/Personal Projects (not Python)/airfoil comparison/Cm_vs_AOA.csv")
ggplot() +
  geom_line(data = df5, aes(x = Alpha, y = NACA_0009, color = "NACA 0009")) +
  geom_point(data = df5, aes(x = Alpha, y = NACA_0009, color = "NACA 0009")) +
  
  geom_line(data = df5, aes(x = Alpha, y = NACA_0012, color = "NACA 0012")) +
  geom_point(data = df5, aes(x = Alpha, y = NACA_0012, color = "NACA 0012")) +
  
  geom_line(data = df5, aes(x = Alpha, y = NACA_2412, color = "NACA 2412")) +
  geom_point(data = df5, aes(x = Alpha, y = NACA_2412, color = "NACA 2412")) +
  
  geom_vline(xintercept = 8, color = "orange", linetype = "dashed", size = 0.5) +
  geom_vline(xintercept = 10, color = "green", linetype = "dashed", size = 0.5) +
  geom_vline(xintercept = 12, color = "lightblue", linetype = "dashed", size = 0.5) +
  
  labs(title = "Moment Coefficient (Cm) vs AOA",
       x = "Angle of Attack (degrees)",
       y = "Moment Coefficient (Cm)",
       color = "Airfoil") +
  theme_minimal()
ggsave("images/cm_vs_aoa.png", width = 10, height = 6, dpi = 300)

cm_mean_0009 <- mean(df5$NACA_0009)
cm_mean_0012 <- mean(df5$NACA_0012)
cm_mean_2412 <- mean(df5$NACA_2412)

n <- 1000
percentages <- 100000 * (100 + runif(n, -2, 2)) / 100

# Save to CSV
write.csv(data.frame(Percentage = percentages), "percentages.csv", row.names = FALSE)


