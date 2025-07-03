library(ggplot2)

# Read the data
df <- read.csv("data/all_naca_cl_vs_cd.csv")

# Plot Cl vs AOA for individual airfoils
ggplot(df, aes(x = AOA_0009, y = Cl_NACA_0009)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for NACA 0009",
       x = "AOA", y = "Cl") +
  theme_minimal()

ggplot(df, aes(x = AOA_0012, y = Cl_NACA_0012)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for NACA 0012",
       x = "AOA", y = "Cl") +
  theme_minimal()

ggplot(df, aes(x = AOA_2412, y = Cl_NACA_2412)) +
  geom_point(color = "black") +
  geom_line(color = "black") +
  labs(title = "Lift Coefficient (Cl) vs AOA for NACA 2412",
       x = "AOA", y = "Cl") +
  theme_minimal()

# Plot Cl/Cd vs AOA for multiple airfoils
ggplot() +
  geom_line(data = df, aes(x = AOA_0009, y = cl_vs_cd_0009, color = "NACA 0009")) +
  geom_point(data = df, aes(x = AOA_0009, y = cl_vs_cd_0009, color = "NACA 0009")) +
  
  geom_line(data = df, aes(x = AOA_0012, y = cl_vs_cd_0012, color = "NACA 0012")) +
  geom_point(data = df, aes(x = AOA_0012, y = cl_vs_cd_0012, color = "NACA 0012")) +
  
  geom_line(data = df, aes(x = AOA_2412, y = cl_vs_cd_2412, color = "NACA 2412")) +
  geom_point(data = df, aes(x = AOA_2412, y = cl_vs_cd_2412, color = "NACA 2412")) +
  
  labs(title = "Cl/Cd vs AOA (Pre-Stall Only)",
       x = "AOA", y = "Cl/Cd", color = "Airfoil") +
  xlim(0, 12) +
  theme_minimal()
