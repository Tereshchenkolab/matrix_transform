library(dplyr)
library(readr)

# Set WD
setwd("") # change to the direct path to your .csv files 

# Bring in and bind all sections and do any additional wrangling (ex. renaming certain columns)


## Section 1. Date/Time/ID data

filepath_datetime <- "Output/datetime"

ds_datetime_1 <- list.files(path=filepath_datetime, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows 

## Section 2. Demographic Data

filepath_demo <- "Output/demog"

ds_demo_2 <- list.files(path=filepath_demo, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows 

## Section 3. Leads

lead_labels <- read_csv("Output/combined_files/leads_12sl_col_labels.csv") %>% pull(1)

filepath_leads <- "Output/leads"

ds_leads_3 <- list.files(path=filepath_leads, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows %>%
  rename_with(~lead_labels)

## Section 4. PQRS Peak info

filepath_pqrs_peak <- "Output/pqrst"

ds_pqrs_peak_4 <- list.files(path=filepath_pqrs_peak, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows 

## Section 5. QRS type info 

filepath_qrs_type <- "Output/qrs"

ds_qrs_type_5 <- list.files(path=filepath_qrs_type, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows %>%
  relocate(EcgID,QRSNUMBER_0,QRSTYP_0,QRSTIM_0,QRSNUMBER_1,QRSTYP_1,QRSTIM_1,QRSNUMBER_2,QRSTYP_2,QRSTIM_2,
           QRSNUMBER_3,QRSTYP_3,QRSTIM_3,QRSNUMBER_4,QRSTYP_4,QRSTIM_4,QRSNUMBER_5,QRSTYP_5,QRSTIM_5,
           QRSNUMBER_6,QRSTYP_6,QRSTIM_6,QRSNUMBER_7,QRSTYP_7,QRSTIM_7,QRSNUMBER_8,QRSTYP_8,QRSTIM_8,
           QRSNUMBER_9,QRSTYP_9,QRSTIM_9,QRSNUMBER_10,QRSTYP_10,QRSTIM_10,QRSNUMBER_11,QRSTYP_11,QRSTIM_11)

## Section 6. Minn info

filepath_minn12 <- "Output/min12sl"

ds_minn12_6 <- list.files(path=filepath_minn12, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows 

## Section 7. EndComments

filepath_end <- "Output/end_comms"

ds_end_7 <- list.files(path=filepath_end, full.names = TRUE) %>% 
  lapply(read_csv, col_types = cols(.default = "c")) %>% 
  bind_rows 

# Final version

ds_final <- ds_datetime_1 %>%
                          left_join(., ds_demo_2,by = "EcgID") %>%
                          left_join(.,ds_leads_3, by = "EcgID") %>%
                          left_join(., ds_pqrs_peak_4,by = "EcgID") %>%
                          left_join(., ds_qrs_type_5,by = "EcgID") %>%
                          left_join(., ds_minn12_6,by = "EcgID") %>%
                          left_join(., ds_end_7,by = "EcgID") %>%
                          relocate(EcgID) %>%
                          write_csv(.,"Output/combined_files/cric_batch2_12sl.csv")
