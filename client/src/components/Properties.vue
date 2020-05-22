<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Properties</h1>
        <hr><br>
        <alert :message="message" v-if="showMessage"></alert>
        <br>
        <el-row class="demo-autocomplete">
          <div class="sub-title">Please type in address:</div>
          <el-autocomplete
            class="w-70 inline-input"
            v-model="selectedPropertyAddress"
            :fetch-suggestions="propertySearch"
            placeholder="Please Input"
            :trigger-on-focus="false"
            @select="handleSelect"
          ></el-autocomplete>
        </el-row>
        <br>
        <table class="table table-hover" v-if="selectedProperty !== null">
          <thead>
            <tr>
              <th scope="col">Full Address</th>
              <th scope="col">Class Description</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ selectedProperty.full_address }}</td>
              <td>{{ selectedProperty.class_description }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="deleteProperty(selectedProperty.property_id)">
                    Delete
                </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      properties: [],
      message: '',
      showMessage: false,
      selectedPropertyAddress: '',
      selectedProperty: null,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getProperties() {
      const path = 'http://localhost:5000/api/properties/';
      axios.get(path)
        .then((res) => {
          this.properties = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    propertySearch(queryString, cb) {
      let properties = [];
      properties = this.properties.map((item) => ({
        value: item.full_address,
        id: item.property_id,
      }));
      const results = queryString ? properties.filter(
        (property) => property.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0,
      ) : properties;
      // call callback function to return suggestions
      cb(results);
    },

    updateProperty(payload, propertyID) {
      const path = `http://localhost:5000/api/properties/${propertyID}`;
      axios.put(path, payload)
        .then((res) => {
          if (Array.isArray(res.data)) {
            this.selectedPropertyAddress = '';
            this.selectedProperty = null;
            this.properties = res.data;
            this.message = 'Property deleted!';
            this.showMessage = true;
          } else {
            this.selectedPropertyAddress = res.data.full_address;
            this.selectedProperty = res.data;
            this.message = 'Property selected!';
            this.showMessage = true;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getProperties();
        });
    },

    handleSelect(item) {
      const payload = {
        property_id: item.id,
        selected: true,
      };
      this.updateProperty(payload, item.id);
    },
    deleteProperty(id) {
      const payload = {
        property_id: id,
        selected: false,
      };
      this.updateProperty(payload, id);
    },
  },
  created() {
    this.getProperties();
  },
};
</script>
<style scoped>
.el-autocomplete {
  width:70% !important;
}
</style>
