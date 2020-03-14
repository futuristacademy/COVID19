# **Modeling the Spread & Impact of COVID-19**
The threat of COVID-19 from spreading and affecting those around us, especially our loved ones that are over the age of 60+ with the exponential mortality rate of COVID 19 rising to 15% in those around the age of 80.

![Air traffic flow 2018](https://preview.redd.it/wevw1wq5gwc31.jpg?width=960&crop=smart&auto=webp&s=870f0423f68d5331f8717eb9e9bc5257b0428e67)

The biggest impact is not only the impact on the health around us, but the stability of the global economy itself.

**Proposal:**
Build the world's richest inter-connected data set that allows the world's smartest researchers to build virus spread models, economic impact models, reporting dashboards, drug vaccine effectiveness models to supply-chain models.

Additional Information Presented by Professor Victor Lee
[Coronavirus-a-serious-need-for-analyzing-connections](https://medium.com/@victor_67825/coronavirus-a-serious-need-for-analyzing-connections-24a4e3de9362)

## COVID-19 Objective 
Enable the Global Community to do something against [COVID-19](https://www.cdc.gov/coronavirus/2019-ncov/about/share-facts.html) which means the only guideline for this Open Source Community Collaboration Project is to build tools and applications that enable others to fight against the Coronavirus.

A good example would be the tool [Sudharshan Ashok](https://www.linkedin.com/in/sudharshanashok/) built called [pyCOVID](https://github.com/sudharshan-ashok/pycovid) a Python package to pull CASE data from the John Hopkins dataset. This Python package acts as an enabler to others on developing their projects. 

## Looking at Participating?
### Getting Started
* Join the [Discord Group](https://discord.gg/KBerGfE) so we can communicate
** Introduce yourself to the community, and let others know where you think you could help out.
* Get access to [COVID19 Repository](https://github.com/futuristacademy/COVID19) (send email to jon.herke@tigergraph.com)

#### As a **researcher** identify and document,
* Reliable data sources
* Supporting publications and research
* Use Cases
* Models

> Add these to README.md or build more .markdown documents on COVID-19 Repository

#### As a **developer** identify, document and build,
* ETL data pipelines (ex. Kafka, Python micro service)
* Scripts or tools (ex. pyCOVID)
* Dashboards (ex. Qlick, Vizlib)
* Applications (ex. Flutter, React)
* Graph Queries (GSQL)

> Contribute code directly to COVID-19 Repository or add component to COVID-19/Awesome.md list 

### Why it’s important to load data into graph
Short read on “[Why it’s important to connect data](http://coronavirus-a-serious-need-for-analyzing-connections/)” → We choose to use a graph database because we can interconnect all the data and make it available to the public via REST endpoints. 

Getting Started with TigerGraph, a look at education materials
https://www.tigergraph.com/certification-graph-fundamentals/
https://www.tigergraph.com/certification-gsql-101/

If you have questions reachout to [jon.herke@tigergraph.com](jon.herke@tigergraph.com) for more information.


**Initiative Community Chat** → [https://discord.gg/KBerGfE](https://discord.gg/KBerGfE)</sub>

**Largest COVID-19 Community Chat** → [https://discord.gg/Bphw4dF](https://discord.gg/Bphw4dF) </sub>



**[Click Here to See Where You Can Help!](https://docs.google.com/document/d/1839IzLW6ao_WUKn9vYu6v6NRpYHPv3Qe7oH8vp3Ec2Y/edit#heading=h.wyg3eofcehe2)**

## Spread Prediction:

### Transportation Data

Viruses spread through means of transportation. The biggest transportation networks are airlines. If we pull the last year of all flight data from every plane to every airport the flew in and out of. Along with the path of virus spread we may begin to identify where the
  

This data can be extracted from OpenSky API.

  
Open Sky Documentation

[https://opensky-network.org/apidoc/rest.html](https://opensky-network.org/apidoc/rest.html)
  

The missing data from open sky is the ICAO which are International Airport Codes

[https://docs.google.com/spreadsheets/d/1CGENTf6vbRkXeXhEuPRq6uIjpNRH_u-0ql5h90qzCoA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1CGENTf6vbRkXeXhEuPRq6uIjpNRH_u-0ql5h90qzCoA/edit?usp=sharing)
  

Sample Data - Pulled from Open Sky [https://colab.research.google.com/drive/16NCKbgVTZIrBj-CasNI7ZycpBZdghJqp#scrollTo=b-flVhevP2IJ](https://colab.research.google.com/drive/16NCKbgVTZIrBj-CasNI7ZycpBZdghJqp#scrollTo=b-flVhevP2IJ)

        [{
        'icao24': 'e48bb0',
        'firstSeen': 1517227957,
        'estDepartureAirport': 'SBSP',
        'lastSeen': 1517229087,
        'estArrivalAirport': None,
        'callsign': 'ONE6004 ',
        'estDepartureAirportHorizDistance': 5036,
        'estDepartureAirportVertDistance': 493,
        'estArrivalAirportHorizDistance': None,
        'estArrivalAirportVertDistance': None,
        'departureAirportCandidatesCount': 1,
        'arrivalAirportCandidatesCount': 0
	    }]
Data restrictions on pulling arrival and departure data is a two hour window. We will need to write a script to pull all the historical data in 2 hour chunks.

### Case Data

The most reliable case data is from John Hopkis whom is pulling World Health Organization data and publishing to their github repository: [https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

  

Case data includes: Province/State, Country/Region ,Last Update, Confirmed, Deaths, Recovered, Latitude, Longitude

Genomic Drug Effectiveness:
Description:
Take a look at current drugs and which ones would be more effective in treating COVID-19. Look at Harmonizome (72 million functional associations between genes and attributes. Use case there have two cases of COVID-19 injected into mice) 

Collect data, include connective weights, find how different molecules are related based on their total biomarker connectivity.

Drug Datasets
ZINC Database: https://zinc.docking.org/
Formatted ZINC Database: https://github.com/molecularsets/moses
DrugBank: https://drugbank.ca
COVID-2019 main protease: https://www.wwpdb.org/pdb?id=pdb_00006lu7
ChemBL: https://www.ebi.ac.uk/chembl/
GenBank COVID-19: https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/
GenBank COVID-19 Meta: https://github.com/nextstrain/ncov/blob/master/data/metadata.tsv
Drug Connectivity Map (CMap): https://clue.io/cmap 
  

## Economic Impact:

Pull Social Media Data?

Pull New Sources Data? (Some listed below)

  

## Trading Data

[http://docs.tradingeconomics.com/#snapshots](http://docs.tradingeconomics.com/#snapshots)

## Additional Data

[https://www.moh.gov.sg/covid-19/](https://www.moh.gov.sg/covid-19/)

[https://www.cdc.gov/coronavirus/2019-ncov/](https://www.cdc.gov/coronavirus/2019-ncov/)

[https://2019ncov.nosugartech.com/data.json](https://2019ncov.nosugartech.com/data.json)

[https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/](https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/)

[https://drive.google.com/file/d/1y3lf7-fiEW_jtoNg_V3rTLn-Ub8yXRcY/view](https://drive.google.com/file/d/1y3lf7-fiEW_jtoNg_V3rTLn-Ub8yXRcY/view)

[https://bnonews.com/index.php/2020/01/the-latest-coronavirus-cases/](https://bnonews.com/index.php/2020/01/the-latest-coronavirus-cases/)

[https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd](https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd)

## TigerGraph Resources

[https://github.com/tigergraph/ecosys](https://github.com/tigergraph/ecosys)

[https://docs.tigergraph.com/](https://docs.tigergraph.com/)

  

### Education Materials:

[https://www.tigergraph.com/certification-graph-fundamentals/](https://www.tigergraph.com/certification-graph-fundamentals/)

[https://www.tigergraph.com/certification-gsql-101/](https://www.tigergraph.com/certification-gsql-101/)

  

### COVID19 Repository

[https://github.com/futuristacademy/COVID19](https://github.com/futuristacademy/COVID19)

  

### COVID Free Server:

[https://covid19.i.tgcloud.io:14240/#/schema-designer](https://covid19.i.tgcloud.io:14240/#/schema-designer)

# Where to Help

**Get Started**

-   Join the [Discord Group](https://discord.gg/KBerGfE) so we can communicate
    
-   Short read on “[Why it’s important to connect data](http://coronavirus-a-serious-need-for-analyzing-connections)”
    
-   If you would like to learn about TigerGraph look at education materials
    

    -   [https://www.tigergraph.com/certification-graph-fundamentals/](https://www.tigergraph.com/certification-graph-fundamentals/)
    
    -   [https://www.tigergraph.com/certification-gsql-101/](https://www.tigergraph.com/certification-gsql-101/)
    

-   Get access to [COVID19 Repository](https://github.com/futuristacademy/COVID19) (send email to [jon.herke@tigergraph.com](mailto:jon.herke@tigergraph.com))
    
-   Get access to this document (send email to jon.herke@tigergraph.com)
    

  

**Data Pipelines:**

-   Setup Data Pipeline for Flight data (Pull from source,Normalization, Push to TG)
    
-   Setup Data Pipeline for Case data (Pull from source,Normalization, Push to TG)
    
-   Determine other data sources
    
-   Setup pipes to other data sources
    

  

**Database:**

-   Sample datasets to build database model (schema)
    
-   Once we have data pipeline create loading job to ingest data
    

  

**Intelligent Layer on top of DB:**

-   Determine what that would look like
    

  
  

**Additional Notes:**

Do we set up a Trello board?
