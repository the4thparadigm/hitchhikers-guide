# ============ Base imports ======================
import os
import glob
# ====== External package imports ================
import yaml
# ====== Internal package imports ================
# ============== Logging  ========================
# =========== Config File Loading ================
# ================================================

# Note: you should change PROJECT_PATH_ENVIRON_VAR to reflect the environment variable 
# 		you made that points to the base directory of the path
projectpath = os.environ['PROJECT_PATH_ENVIRON_VAR']
# Config files assumed to be under config subdirectory
config_path = os.path.join(projectpath, "config/")


def get_config():
    conf = Configuration()
	# Read all yaml files in the config directory and add their contents to the config file
	conf = {}
    for config_file in glob.glob(f"{config_path}*.yml") + glob.glob(f"{config_path}*.yaml"):
		fname = os.path.splittext(os.path.basename(config_file))
        conf[fname] = yaml.load(open(config_file)))
    return conf


def main():
    test = get_config()
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
