package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path"

	"gopkg.in/yaml.v2"
)

type Config struct {
	RepositoryName string
	GroupsConfig GroupsConfig
	SoftwareListConfig SoftwareListConfig
	MicroserviceConfigs []MicroserviceConfig
}

type GroupsConfig struct {
  GroupsConfig []MicroservicGroupConfig `yaml:"groups"`
}

type MicroservicGroupConfig struct {
	Name	string `yaml:"name"`
	Microservices	[]string `yaml:"microservices"`
}

type SoftwareListConfig struct {
	SoftwareConfigs []SoftwareConfig `yaml:"softwarelist"`
}

type SoftwareConfig struct {
	Name string `yaml:"name"`
	SoftwareKey string `yaml:"software"`
	Version string `yaml:"version"`
}

type MicroserviceConfig struct {
	Name string `yaml:"name"`
	Runner string `yaml:"runner"`
	Path []string `yaml:"path"`
	Groups []string `yaml:"groups"`
}

func ParseConfig() (*Config, error) {
	repoPath, err := os.Getwd()
  if err != nil {
    log.Fatalf("OS Error. Cannot get working directory")
  }

  // TODO: Make this smarter
  micromPath := path.Join(path.Dir(repoPath), ".microm")

  config := new(Config)
  config.RepositoryName = path.Base(path.Dir(micromPath))
  groups, err := parseGroups(micromPath)
  if err != nil {
    return config, fmt.Errorf("failed to parse groups from the microm config %v", err) 
  }
  config.GroupsConfig = *groups

  config.MicroserviceConfigs, err = parseMicroserviceConfigs(micromPath)
  if err != nil {
    return config, fmt.Errorf("failed to parse microservices from the microm config %v", err) 
  }

  softwareConfigs, err := parseSoftwareConfigs(micromPath)
  if err != nil {
    return config, fmt.Errorf("failed to parse software list from the microm config %v", err) 
  }
  config.SoftwareListConfig = *softwareConfigs

  return config, nil
}

func parseGroups(micromPath string) (*GroupsConfig, error) {
  groupsPath := path.Join(micromPath, "groups.yaml")
  yamlFile, err := ioutil.ReadFile(groupsPath)
  if err != nil {
    return nil, fmt.Errorf("error reading groups file: %v ", err)
  }

  var groups *GroupsConfig
  err = yaml.Unmarshal(yamlFile, &groups)
  if err != nil {
    return nil, fmt.Errorf("error unmarshalling groups file: %v ", err)
  }
	
  return groups, nil
}

func parseMicroserviceConfigs(micromPath string) ([]MicroserviceConfig, error) {
  microservicesPath := path.Join(micromPath, "microservices")
  microserviceDirs, err := ioutil.ReadDir(microservicesPath)
  if err != nil {
    return nil, fmt.Errorf("error reading microservice dir: %v ", err)
  }

  var microservices []MicroserviceConfig

  for _, microserviceDir := range microserviceDirs {
    valuesFile := path.Join(microservicesPath, microserviceDir.Name(), "values.yaml")

    yamlFile, err := ioutil.ReadFile(valuesFile)
    if err != nil {
      return nil, fmt.Errorf("error reading groups.yaml file: %v ", err)
    }

    microservice := new(MicroserviceConfig)
    err = yaml.Unmarshal(yamlFile, microservice)
    if err != nil {
      return nil, fmt.Errorf("error unmarshalling values.yaml file: %v ", err)
    }
    microservices = append(microservices, *microservice)
  }

  return microservices, nil 
}

func parseSoftwareConfigs(micromPath string) (*SoftwareListConfig, error) {
  softwareListPath := path.Join(micromPath, "software.yaml")
  yamlFile, err := ioutil.ReadFile(softwareListPath)
  if err != nil {
    return nil, fmt.Errorf("error reading software.yaml file: %v ", err)
  }

  var softwareList *SoftwareListConfig
  err = yaml.Unmarshal(yamlFile, &softwareList)
  if err != nil {
    return nil, fmt.Errorf("error unmarshalling software.yaml file: %v ", err)
  }
	
  return softwareList, nil
}