# VUE

Vue.js是一种用于构建用户界面的渐进式JavaScript框架。Vue被设计为可以自底向上逐层应用。Vue的核心库只关注视图层，不仅易于上手，也便于与第三方库或现有项目整合。以下是Vue的一些主要特性：

### 响应式数据绑定

Vue最显著的特性之一是其响应式系统。当Vue实例的数据对象的属性被访问和修改时，视图会自动更新。

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

这会导致具有`id="app"`的DOM在其内容中显示“Hello Vue!”。如果`vm.message`的值改变，DOM会自动更新。

### 组件系统

Vue使用组件系统，允许开发者构建可复用的组件，每个组件都可以有自己的视图、数据逻辑和样式。

```javascript
Vue.component('todo-item', {
  template: '<li>这是一个待办项</li>'
})

var app = new Vue(...)
```

### 虚拟DOM

Vue.js使用**虚拟DOM**来渲染**视图**。这意味着Vue构建一个**轻量级的内存中DOM表示**，**计算出最小的必要DOM更新，然后进行必要的DOM操作，这种方式可以提高渲染效率。**

### 模板

Vue使用基于HTML的模板语法，允许开发者声明式地将DOM绑定至底层Vue实例的数据。所有Vue.js模板都是合法的HTML，所以可以被遵循规范的浏览器和HTML解析器解析。

```html
<div id="app">
  {{ message }}
</div>
```

### 计算属性和侦听器

计算属性是依赖于响应式数据变化而自动更新的值。侦听器（**watchers**）则允许执行代码响应于数据的变化。

```javascript
var vm = new Vue({
  el: '#app',
  data: {
    a: 1
  },
  computed: {
    // 计算属性的 getter
    b: function () {
      // `this` 指向 vm 实例
      return this.a + 1
    }
  }
})
```

### 指令（Directives）

Vue指令（例如**v-bind和v-on**）提供了**声明式的方法来将DOM元素的行为绑定到数据模型上**。这些指令前缀为`v-`。

```html
<div id="app">
  <!-- 绑定属性 -->
  <img v-bind:src="imageSrc">
  
  <!-- 绑定事件 -->
  <button v-on:click="doSomething">
    Click me!
  </button>
</div>
```

### 过渡 & 动画

Vue提供了过渡的应用方式，通过包裹要动画化的组件或元素，在CSS过渡和动画中自动应用类名。

```html
<div id="demo">
  <button v-on:click="show = !show">
    Toggle
  </button>
  <transition name="fade">
    <p v-if="show">hello</p>
  </transition>
</div>
```

### 路由 Vue Router

**通过Vue Router，Vue.js提供了前端路由的解决方案，用于构建单页面应用（SPA）。**

```javascript
const router = new VueRouter({
  routes: [
    { path: '/foo', component: Foo },
    { path: '/bar', component: Bar }
  ]
})
```

- #### 核心概念

1. **路由和路由器**：
   - **路由（Route）**：路由是一个映射关系，**它定义了 URL 到组件的映射。每个路由都可以关联到一个或多个 Vue 组件。**
   - **路由器（Router）**：路由器是管理所有路由的容器，它负责监听 URL 的变化，并根据当前的 URL 显示相应的组件。
2. **动态路由匹配**：
   - Vue Router 允许你定义动态路径参数，这些参数以冒号 `:` 开始。例如，`/user/:id` 可以匹配 `/user/1` 或 `/user/2`。
3. **嵌套路由**：
   - 可以创建基于组件的嵌套路由，以构建更复杂的应用布局。
4. **编程式和声明式导航**：
   - **声明式导航**：使用 `<router-link>` 组件来导航。
   - **编程式导航**：使用 `router.push` 或 `router.replace` 方法在 JavaScript 代码中导航。
5. **路由守卫**：
   - 提供了全局守卫、路由独享守卫和组件内守卫，用于控制导航的过程，实现例如认证、权限检查等功能。

#### 使用方法

1. **创建路由实例**：
   - 创建一个路由实例，并定义路由规则。

```js
import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './components/Home.vue';
import About from './components/About.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
];

const router = new VueRouter({
  routes,
  mode: 'history' // 使用 HTML5 History 模式
});
```

1. 连接到 Vue 实例
   - 将路由实例注入到 Vue 根实例中。

```js
import Vue from 'vue';
import App from './App.vue';
// 假设 router 实例已经创建
import router from './router';

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
```

1. 使用 `<router-view>` 和 `<router-link>`
   - `<router-view>` 是一个容器组件，用于渲染当前路由对应的组件。
   - `<router-link>` 用于创建导航链接，它会被渲染为一个 `<a>` 标签。



### 状态管理 Vuex

Vuex是Vue应用程序的状态管理模式和库，它**为应用中的所有组件提供了一个集中存储服务。**

```javascript
const store = new Vuex.Store({
  state: {
    count: 1
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})
```



当然，我很乐意为您详细介绍 Vuex。

- #### Vuex 是什么？


Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式和库。它作为一个集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 非常适合用于中大型单页应用（SPA），因为这类应用通常需要在多个组件间共享状态。

- #### Vuex 的核心概念

**Vuex 的设计和 Redux 类似**，但它利用了 Vue.js 的细粒度数据响应机制来进行高效的状态更新。以下是 Vuex 的一些核心概念：

1. **State（状态）**:
   - State 是单一状态树，用于存储整个应用的状态。
   - 它是响应式的，当 Vue 组件从 store 中读取状态时，若 state 中的对象发生改变，相应的组件也会自动更新。

2. **Getters（获取器）**:
   - Getters 允许你从 state 中派生出一些状态，例如对列表进行过滤并计数。
   - 它们是作为 store 的计算属性。

3. **Mutations（变更）**:
   - Mutations 用于更改状态，它是同步事务。
   - 你不能直接调用一个 mutation，而是需要以 `type` 的形式调用 `store.commit` 方法。

4. **Actions（动作）**:
   - Actions 类似于 mutations，不同在于它们可以包含任意异步操作。
   - Actions 可以调用 `store.commit` 提交一个 mutation，或者触发更多的 action。

5. **Modules（模块）**:
   - Vuex 允许将 store 分割成模块，每个模块拥有自己的 state、mutations、actions、getters，甚至是嵌套子模块。

- #### 如何使用 Vuex？


在 Vue.js 应用中使用 Vuex 大致步骤如下：

2. **创建一个 Store**:
   - Store 是存储应用状态的地方。你需要定义一个新的 Vuex Store，并将其状态和 mutations 定义好。

3. **在 Vue 组件中使用 Store**:
   - 组件通过 **`this.$store` 访问 Vuex store，从 store 的 state 中读取状态，通过 mutations 更改状态。**

4. **在根实例中注入 Store**:
   - 创建 Vue 根实例时，将 store 注入，这样所有的子组件都可以使用 store。



以下是一个简单的 Vuex 使用示例：

```javascript
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  }
});

new Vue({
  el: '#app',
  store,
  methods: {
    increment() {
      this.$store.commit('increment');
    }
  }
});
```

**Vuex 提供了一种集中式存储管理应用的所有组件状态的方法，并以特定的规则保证状态以可预测的方式发生变化**。这对于在多个组件之间共享状态的复杂应用来说，是非常有用的。通过使用 Vuex，Vue 应用程序的代码和组件可以更加高效和有序。



### 模板语法和数据绑定

模板语法是在前端框架中使用的一种**标记语法**，它允许开发者**嵌入基于特定逻辑的动态值和数据到HTML结构中**。在模板语法中，你通常会见到**特殊的标记或字符，这些标记告诉框架应该在这些地方插入或执行JavaScript表达式的结果。**

模板语法通常包括以下几种表达方式：

1. ### 插值

- **文本插值**：最常见的是使用双花括号 `{{ ... }}` 进行文本插值，展示JavaScript表达式的值。

  ```html
  <p>{{ message }}</p>
  ```

  在Vue或Angular中，这会在`<p>`元素中输出`message`变量的值。

1. ### 指令

- **属性绑定**：使用特殊的前缀（如Vue中的`v-bind:`或Angular中的`[]`）来绑定属性到表达式的值。

  ```html
  <!-- 在 Vue 中 -->
  <a v-bind:href="url">Link</a>
  
  <!-- 在 Angular 中 -->
  <a [href]="url">Link</a>
  ```

- **事件绑定**：使用特殊的前缀（如Vue中的`v-on:`或Angular中的`()`）来绑定事件监听器。

  ```html
  <!-- 在 Vue 中 -->
  <button v-on:click="doSomething">Click me</button>
  
  <!-- 在 Angular 中 -->
  <button (click)="doSomething()">Click me</button>
  ```

1. ### 循环与条件语句

- **循环**：使用特殊指令循环渲染一个元素列表。

  ```html
  <!-- 在 Vue 中 -->
  <ul>
    <li v-for="item in items">{{ item.text }}</li>
  </ul>
  
  <!-- 在 Angular 中 -->
  <ul>
    <li *ngFor="let item of items">{{ item.text }}</li>
  </ul>
  ```

- **条件渲染**：根据表达式的真值来决定是否渲染元素。

  ```html
  <!-- 在 Vue 中 -->
  <p v-if="seen">Now you see me</p>
  
  <!-- 在 Angular 中 -->
  <p *ngIf="seen">Now you see me</p>
  ```



### v-model 双向数据绑定

**对于表单输入和应用状态之间的双向数据绑定，Vue提供了一个指令`v-model`。这大大简化了数据在用户输入表单和应用状态之间的同步。**`v-model` 是 Vue.js 中用于创建双向数据绑定的一个指令。主要用于表单元素（如 `<input>`、`<select>` 和 `<textarea>`），它确保了输入控件的值和数据模型中的值保持同步。

```html
<input v-model="message" placeholder="edit me">
<p>The message is: {{ message }}</p>
```

在这个例子中，`message`属性会与`<input>`的值保持同步。

- #### `v-model` 的工作原理


1. **数据到视图的绑定**：
   - **当数据模型的值发生变化时，`v-model` 确保这个变化反映到视图上，即更新对应的表单元素的显示值。**

2. **视图到数据的绑定：**
   - **当用户与表单元素交互（例如输入文本、选择选项等）时，`v-model` 确保视图上的改变更新到数据模型中。这通常通过监听 DOM 事件（如 `input`、`change`）来实现。**

- #### 底层原理


1. **数据绑定**：
   - Vue.js 使用了响应式系统，其中对象的属性被转换为 **getter/setter**，以便 Vue 可以追踪依赖并在属性值变更时通知视图更新。
   - 当你在数据模型中定义一个属性，并在模板中用 `v-model` 绑定它，Vue 就会自动确保模型和视图间的同步。

2. **事件监听**：
   - `v-model` 实际上是一个语法糖，它结合了 `:value`（数据到视图的绑定）和 `@input`（视图到数据的绑定）。
   - 对于不同的表单元素，`v-model` 会使用不同的事件和属性。例如，对于 `<input type="text">`，它使用 `value` 属性和 `input` 事件；而对于 `<checkbox>`，它使用 `checked` 属性和 `change` 事件。

3. **组件内的 v-model**：
   - 当在自定义组件上使用 `v-model` 时，它默认绑定到组件的 `value` 属性并监听 `input` 事件。
   - 开发者可以通过组件的 `props` 和 `$emit` 自定义 `v-model` 的行为。

- #### 示例


假设有一个 Vue 组件，其中包含一个文本输入框，你可以使用 `v-model` 来创建数据绑定：

```vue
<template>
  <input v-model="message">
</template>

<script>
export default {
  data() {
    return {
      message: ''
    };
  }
}
</script>
```

在这个例子中，`message` 属性与文本框的值绑定。当用户在文本框中输入时，`message` 的值会实时更新；反过来，如果 `message` 的值在其他地方被改变，文本框的显示内容也会相应更新。

- #### 总结

`v-model` 提供了一种简洁高效的方法来实现数据和视图的双向绑定。它是基于 Vue.js 的响应式系统和事件处理机制构建的，大大简化了表单数据处理的复杂性。通过 `v-model`，开发者可以更加专注于数据逻辑，而不是繁琐的 DOM 操作。



### 组件的动态和异步加载

Vue允许你以动态和异步的方式加载组件。这对于加载大型应用程序，尤其是那些需要代码分割和懒加载的应用程序非常有用。

```javascript
Vue.component('async-webpack-example', function (resolve, reject) {
  // 这个特殊的 `require` 语法将会告诉 webpack
  // 自动将你的构建代码切割成多个包，这些包
  // 会通过 Ajax 请求加载
  require(['./my-async-component'], resolve)
})
```



### 生命周期钩子

Vue.js是一个流行的JavaScript框架，它为开发者提供了一系列的生命周期钩子（也称为生命周期方法）。这些钩子在Vue组件的不同阶段被自动调用，允许**开发者在特定时刻添加他们自己的代码，进行状态管理、DOM操作、数据获取等任务。**

以下是Vue组件的主要生命周期钩子及其用途的详细介绍：

**1. `beforeCreate`**

- 在实例初始化之后、数据观测 (data observation) 和事件/侦听器配置之前被调用。
- 在这个阶段，data、computed、methods、watch等还没有被设置。

**2. `created`**

- 在实例创建完成后被立即调用。
- 在这个阶段，Vue实例已完成数据观测、属性和方法的运算、watch/event事件回调的配置。
- 这个钩子在服务端渲染期间也会被调用。

**3. `beforeMount`**

- 在挂载开始之前被调用：相关的`render`函数首次被调用。
- 这是在模板编译成HTML后、挂载DOM之前的最后一刻，可以对数据进行最后的更改。

**4. `mounted`**

- `el` 被新创建的 `vm.$el` 替换，并挂载到实例上去之后调用该钩子。
- 在这个阶段，你可以访问到完整的渲染DOM。
- 这个钩子在服务端渲染期间不会被调用。

**5. `beforeUpdate`**

- 在数据变化后、DOM被重新渲染和更新之前调用。
- 这个钩子可以用来在当前的DOM更新之前执行依赖于DOM的操作。

**6. `updated`**

- 在由于**数据更改导致的虚拟DOM重新渲染和打补丁之后调用。**
- 当这个钩子被调用时，组件DOM已经更新，因此你可以执行依赖于DOM的操作。
- 然而，这个时期可能会在某些子组件还没更新完成时就被调用。

**7. `beforeDestroy`**

- 在实例销毁之前调用。在这一步，实例仍然完全可用。
- 这是清理事件监听器、定时器或执行其他清理任务的好时机。

**8. `destroyed`**

- 在实例销毁后调用。调用后，Vue实例指示的所有东西都会解绑定，所有的事件监听器被移除，所有的子实例也都会被销毁。
- 这个钩子在服务端渲染期间不会被调用。

**9. `activated` 和 `deactivated`**

- 用于`<keep-alive>`包裹的动态组件。
- `activated` 在组件被激活时调用，`deactivated` 在组件被停用时调用。

```vue
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Hello Vue!",
    };
  },
  // beforeCreate
  beforeCreate() {
    console.log("beforeCreate: 组件实例刚被创建，属性和方法尚未初始化");
  },
  // created
  created() {
    console.log("created: 组件实例已创建，属性和方法已初始化");
    // 此时可以进行数据请求或开始定时任务
  },
  // beforeMount
  beforeMount() {
    console.log("beforeMount: 模板编译/挂载之前");
  },
  // mounted
  mounted() {
    console.log("mounted: 组件已挂载到DOM，可以进行DOM操作");
  },
  // beforeUpdate
  beforeUpdate() {
    console.log("beforeUpdate: 组件更新之前");
  },
  // updated
  updated() {
    console.log("updated: 组件更新之后");
  },
  // beforeDestroy
  beforeDestroy() {
    console.log("beforeDestroy: 组件销毁之前");
    // 清理工作，如清除定时器或解绑事件监听器
  },
  // destroyed
  destroyed() {
    console.log("destroyed: 组件销毁之后");
  },
};
</script>

```



### 提供/注入机制

提供/注入机制是一种高级的用于跨多个组件传递数据的方式，通常在深层嵌套的组件中使用，作为传递props的替代方案。

```javascript
// 父组件提供 'foo'
var Provider = {
  provide: {
    foo: 'bar'
  },
  // ...
}

// 子组件注入 'foo'
var Child = {
  inject: ['foo'],
  created() {
    console.log(this.foo) // => "bar"
  }
  // ...
}
```



## VUE2和VUE3

### **webpack和vite**

① vue2使用的是**webpack**形式去构建项目
webpack是一开始是入口文件，然后分析路由，然后模块，最后进行打包，然后告诉你，服务器准备好了可以开始干了
②vue3使用**vite**构建项目
先告诉你服务器准备完成，然后等你发送HTTP请求，然后是入口文件，Dynamic import（动态导入）code split point（代码分割）

最大的好处和区别就是为了让项目中一些代码文件多了以后去保存更新数据时更快能够看到实际效果，也就是所谓的（**热更新**）



#### Vite 

Vite 是一个由尤雨溪（Evan You）开发的现代前端构建工具，旨在提供更快的开发体验。它是一个基于 ES 模块的构建工具，能够**显著提升前端项目的启动速度和热更新（Hot Module Replacement, HMR）的性能**。下面是 Vite 的主要特点和工作原理的详细介绍：

1. **快速的冷启动**：
   - 传统的打包工具（如 **Webpack**）在项目启动时**需要对整个应用进行打包，这在大型项目中可能很慢**。Vite 利用浏览器原生 ES 模块导入，只需要对请求的模块进行转换，从而实现快速的冷启动。

2. **即时的模块热更新（HMR）**：
   - Vite 提供了快速的热模块替换，当文件发生变化时，只有受影响的模块会重新加载和渲染，而不是整个页面。

3. **丰富的插件生态和易用的 API**：
   - Vite 支持 Rollup 插件，这意味着开发者可以利用 Rollup 已有的丰富插件生态。同时，Vite 自身也提供了简单易用的 API 来开发新插件。

4. **内置开发服务器和构建功能**：
   - Vite 自带一个开发服务器，支持诸如 TypeScript、JSX、CSS 预处理器等现代 Web 技术，无需额外配置。对于生产环境构建，Vite 使用 Rollup 进行打包，优化输出结果。

5. **预打包依赖**：
   - Vite 会预先打包 `node_modules` 中的依赖，这使得开发服务器的启动更快，依赖更新时也只需要重新打包改变的部分。

6. **支持 TypeScript、JSX 等**：
   - Vite 支持使用 TypeScript 和 JSX，无需额外的插件或配置。

- #### 工作原理


1. **基于浏览器原生 ES 模块**：
   - Vite 利用了现代浏览器对 ES 模块的原生支持。在开发模式下，Vite 服务器会将源码中的 `import` 语句转换为浏览器可以直接加载的 URL。

2. **依赖预打包**：
   - 对于 `node_modules` 中的第三方库，**Vite 使用 esbuild 预先打包这些库**。esbuild 是一个非常快速的 JavaScript 打包器和最小化工具，**这大大加快了初始加载时间和热更新速度。**

3. **模块热更新（HMR）**：
   - Vite 的 HMR 实现通过 WebSocket 与浏览器通信。当源代码更改时，Vite 只会重新加载更改的部分，而不是整个应用。

4. **生产构建**：
   - 对于生产环境的构建，Vite 使用 Rollup 进行打包。Rollup 是一个成熟的打包工具，专注于生成尽可能小的打包文件，同时支持高度可配置的插件系统。

- #### 使用 Vite


1. **安装和创建新项目**：
   - 可以使用 `npm init vite@latest` 命令来创建一个新项目，选择合适的模板（如 Vue、React）。

2. **配置**：
   - Vite 的配置文件是 `vite.config.js`，它提供了丰富的配置选项，例如定义别名、配置代理、定制插件等。

3. **开发和构建**：
   - 使用 `vite` 命令启动开发服务器，使用 `vite build` 进行项目构建。



#### Webpack

Webpack 是一个现代 JavaScript 应用程序的静态模块打包器。在 Webpack 处理应用程序时，它会递归地构建一个依赖关系图，其中包括应用程序需要的每个模块，然后将所有这些模块打包成一个或多个 bundle。

- #### 核心概念


1. **入口（Entry）**：
   - 定义了 Webpack 开始构建的起点。

2. **输出（Output）**：
   - 指示 Webpack 如何以及在哪里输出打包后的文件。

3. **加载器（Loaders）**：
   - 让 Webpack 能够去处理那些非 JavaScript 文件（Webpack 本身只理解 JavaScript）。

4. **插件（Plugins）**：
   - 扩展了 Webpack 的功能，它们在整个构建过程的不同阶段执行广泛的任务。

5. **模式（Mode）**：
   - 设置 `mode` 参数（如 `development` 或 `production`），以启用 Webpack 的内置优化。

6. **模块（Module）**：
   - Webpack 中的模块是其核心概念，它可以是项目中的任何类型的文件。



- #### 特点

- **代码拆分（Code Splitting）**：

  - Webpack 有能力拆分代码到不同的 bundle 中，然后可以按需加载，或并行加载这些文件。

- **加载器和插件系统**：

  - 强大的加载器和插件系统使得 Webpack 非常灵活，能够处理各种类型的资源。

- **开发中间件**：

  - 如 `webpack-dev-server` 和 `webpack-hot-middleware` 提供了开发服务器和热更新功能。



#### Webpack 与 Vite 对比

1. **启动速度**：

   - **Webpack**：对于大型项目，Webpack 的启动速度可能较慢，因为需要打包整个应用程序。

- **Vite**：提供快速的启动速度，特别是在大型项目中，因为它利用了浏览器的原生 ES 模块功能，只加载需要的模块。

2. **热模块替换（HMR）**：

   - **Webpack**：支持 HMR，但性能会随着项目的增大而降低。
   - **Vite**：提供更快的 HMR，因为它只需重新加载改变的模块。

3. **构建时间**：

   - **Webpack**：在生产环境的构建过程中，可能需要更多时间进行优化、代码拆分等任务。
   - **Vite**：使用 Rollup 进行生产构建，通常比 Webpack 快，特别是在进行树摇（tree-shaking）和代码拆分时。

4. **兼容性**：

   - **Webpack**：由于存在更长时间，拥有广泛的插件生态和社区支持，对旧版浏览器的兼容性更好。
   - **Vite**：专注于现代 JavaScript，可能不适用于需要兼容老版本浏览器的项目。

5. **配置复杂性**：

   - **Webpack**：配置相对复杂，特别是对于复杂的项目。
   - **Vite**：提供了更简单的配置体验，大多数情况下开箱即用。

6. **使用场景**：

   - **Webpack**：是一个成熟的工具，适用于需要复杂构建逻辑和广泛插件支持的大型项目。它的灵活性和插件生态系统使其成为当前很多项目的首选。

   - **Vite**：提供了对现代前端开发的优化，特别是在快速开发和轻松配置方面。它利用了最新的 Web 技术，如原生 ES 模块，从而在开发体验和性能上提供了显著优势。

     对于新项目，特别是那些以现代浏览器为目标的项目，Vite 可能是一个更好的选择。对于已有的大型项目，或者对老旧浏览器兼容性有要求的项目，Webpack 可能更为合适。



### **main.js文件**

vue2中我们可以使用**pototype**(原型)的形式去进行操作，引入的是构造函数
vue3中需要使用**结构的形式进行操作**，引入的是**工厂函数**
**vue3中app组件中可以没有根标签**



### **指令与插槽**

vue2中使用slot可以直接使用slot,而vue3中必须使用v-slot的形式
v-for与v-if在vue2中优先级高的是v-for指令，而且不建议一起使用
vue3中v-for与v-if,只会把当前v-if当做v-for中的一个判断语句，不会相互冲突
vue3中移除keyCode作为v-on的修饰符，当然也不支持config.keyCodes
vue3中移除v-on.native修饰符
vue3中移除过滤器filter



### 生命周期

对于生命周期来说，整体上变化不大，只是大部分生命周期钩子名称上 + “on”，功能上是类似的。不过有一点需要注意，Vue3 在组合式API（Composition API，下面展开）中**使用生命周期钩子时需要先引入**，而 Vue2 在选项API（Options API）中可以**直接调用生命周期钩子**，如下所示。

```js
js复制代码// vue3
<script setup>     
import { onMounted } from 'vue';   // 使用前需引入生命周期钩子
 
onMounted(() => {
  // ...
});
 
// 可将不同的逻辑拆开成多个onMounted，依然按顺序执行，不会被覆盖
onMounted(() => {
  // ...
});
</script>
 
// vue2
<script>     
export default {         
  mounted() {   // 直接调用生命周期钩子            
    // ...         
  },           
}
</script> 
```

常用生命周期对比如下表所示。

| vue2          | vue3            |
| ------------- | --------------- |
| beforeCreate  |                 |
| created       |                 |
| beforeMount   | onBeforeMount   |
| mounted       | onMounted       |
| beforeUpdate  | onBeforeUpdate  |
| updated       | onUpdated       |
| beforeDestroy | onBeforeUnmount |
| destroyed     | onUnmounted     |

> Tips： setup 是围绕 beforeCreate 和 created 生命周期钩子运行的，所以不需要显式地去定义



vue2中我们是通过new Vue(),在执行beforeCreate与created接着问你有没有vm.$mount(el)
<img src="https://img-blog.csdnimg.cn/4c416962491b4ea4a3d89d501e2c89f7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQmlLQUJp,size_20,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述" style="zoom: 50%;" />
vue3中是先准备好所有后再执行
<img src="https://img-blog.csdnimg.cn/28e70c06d9d54e129310acb83c465e6c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQmlLQUJp,size_20,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述" style="zoom:50%;" />
区别：**beforeCreate与created并没有组合式API中,setup就相当于这两个生命周期函数**



### 响应式原理的区别

Vue.js 是一个流行的前端框架，其核心特性之一就是响应式系统。Vue 2 和 Vue 3 在实现响应式方面有着显著的差异。

- #### Vue 2 的响应式原理


Vue 2 使用了 **Object.defineProperty** 方法来实现响应式系统。它的工作原理如下：

1. **数据劫持（Data Hijacking）**：Vue 2 通过 `Object.defineProperty` 方法对组件的数据对象进行遍历，将所有的属性转换为 getter/setter。这样 Vue 就能够追踪属性的读取和修改。

2. **依赖收集（Dependency Collection）**：当渲染函数被执行时，Vue 会追踪正在读取的属性，这些属性被认为是渲染函数的依赖。

3. **观察者模式（Observer Pattern）**：每个组件实例都有一个观察者（watcher）实例，它会记录组件的依赖并在依赖项发生改变时触发更新。

4. **更新视图**：当数据发生改变时，setter 方法会被调用，触发依赖于该数据的视图更新。

Vue 2 的响应式系统有一些限制，如无法检测到对象属性的添加或删除、数组索引和长度的变化等。

- #### Vue 3 的响应式原理


Vue 3 引入了 **Proxy** 作为其响应式系统的基础，这带来了显著的改进。其原理包括：

1. **使用 Proxy**：Vue 3 使用 ES6 的 `Proxy` 对象重写了响应式系统。`Proxy` 可以直接监听对象和数组的变化，包括属性的添加、删除和数组索引的修改。

2. **反应性跟踪（Reactivity Tracking）**：当一个组件的状态被访问时，Vue 3 使用 `Proxy` 的 getter 方法来追踪依赖，使用 setter 方法来检测变化并触发更新。

3. **更好的性能**：由于 `Proxy` 能够更精确地追踪变化，Vue 3 的响应式系统比 Vue 2 更高效。它不需要初始化时遍历所有的属性，也能够处理动态添加的属性。

4. **Composition API**：Vue 3 引入了 Composition API，它提供了一个更灵活的方式来组织组件的逻辑。这与响应式系统紧密集成，允许更精细的控制响应式行为。



### 多根节点

熟悉 Vue2 的朋友应该清楚，在模板中如果使用多个根节点时会报错，如下所示。

```js
// vue2中在template里存在多个根节点会报错
<template>
  <header></header>
  <main></main>
  <footer></footer>
</template>
 
// 只能存在一个根节点，需要用一个<div>来包裹着
<template>
  <div>
    <header></header>
    <main></main>
    <footer></footer>
  </div>
</template>
```

但是，Vue3 支持多个根节点，也就是 fragment。即以下多根节点的写法是被允许的。

```js
<template>
  <header></header>
  <main></main>
  <footer></footer>
</template>
```



### Options API和Composition API

Vue2 是选项API（Options API），**一个逻辑会散乱在文件不同位置（data、props、computed、watch、生命周期钩子等）**，导致代码的可读性变差。当需要修改某个逻辑时，需要上下来回跳转文件位置。

Vue3 组合式API（Composition API）则很好地解决了这个问题，**可将同一逻辑的内容写到一起**，增强了代码的可读性、内聚性，其还提供了较为完美的逻辑复用性方案。



- #### 选项式 API 示例

在选项式 API 中，我们通常会定义一个 `data` 对象来存储组件的状态，定义 `methods` 来处理用户交互，使用 `computed` 属性来定义依赖于组件状态的计算属性。

```javascript
<template>
  <div>
    <p>{{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    increment() {
      this.count++;
    },
  },
};
</script>
```

在这个例子中，我们有一个简单的计数器，它的状态（`count`）和方法（`increment`）都是通过组件的选项来定义的。



- #### 组合式 API 示例

组合式 API 使用 `setup` 函数来组织组件的逻辑。在 `setup` 函数中，我们可以使用 `reactive` 或 `ref` 来定义响应式状态，使用普通函数来处理事件。

```javascript
<template>
  <div>
    <p>{{ count.value }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(0);

    function increment() {
      count.value++;
    }

    return {
      count,
      increment,
    };
  },
};
</script>
```

在这个例子中，我们同样实现了一个计数器。不同的是，我们使用了组合式 API 的 `setup` 函数，其中 `count` 是一个 `ref` 对象，这使得它成为响应式的。我们直接在 `setup` 函数中定义了 `increment` 函数，并将这些变量和函数返回，使它们在模板中可用。

- **代码组织**：在选项式 API 中，相关的逻辑（比如与 `count` 相关的数据和方法）是分散在不同选项中的。而在组合式 API 中，相关逻辑可以更容易地组织在一起。

- **逻辑复用**：组合式 API 更容易在组件之间复用逻辑。你可以将相关的逻辑抽象成一个函数，然后在多个组件中重用它。

- **类型推断**：组合式 API 对于使用 TypeScript 的项目更友好，因为它能提供更好的类型推断。

- **适用场景**：选项式 API 适合于简单或中等复杂度的应用，而组合式 API 适合于需要更复杂逻辑组织的大型应用。

理解这两种 API 的不同之处不仅有助于更好地使用 Vue.js，还能帮助你根据项目需求选择最合适的方法来构建你的应用。



## VUE和REACT的优势与劣势

### React

- #### 技术特性

1. **虚拟DOM**：React使用虚拟DOM来优化DOM操作，提高渲染效率。
2. **组件化结构**：React强调可复用的组件，使得代码更加模块化和易于维护。
3. **JSX**：React使用JSX语法，允许在JavaScript代码中写入HTML结构。
4. **单向数据流**：React采用单向数据流，这使得数据状态管理更加清晰。
5. **Hooks**：React引入Hooks使得在函数组件中使用状态和其他React特性变得可能，极大地提高了函数组件的能力。

- #### 技术优势

1. **高效的更新机制**：虚拟DOM的使用可以减少对实际DOM的操作，提高应用性能。
2. **丰富的生态系统**：有大量的第三方库和工具可供选择。
3. **强大的社区支持**：由于Facebook的支持，React有着非常活跃的社区和良好的维护。

- #### 技术局限性

1. **JSX的学习曲线**：JSX混合了HTML和JavaScript，对于初学者可能稍显复杂。
2. **状态管理**：在大型应用中，状态管理（如使用Redux）可能会变得复杂。

### Vue

- #### 技术特性

1. **响应式系统**：Vue的响应式系统可以自动追踪依赖关系并在数据变化时更新视图。
2. **模板语法**：Vue使用基于HTML的模板语法，易于学习和使用。
3. **组件化**：Vue同样强调组件化，促进了代码的复用和模块化。
4. **单文件组件**：Vue的单文件组件（.vue文件）将模板、脚本和样式封装在一起，便于组织代码。
5. **Vue CLI**：提供了强大的命令行工具，用于快速生成项目模板。

- #### 技术优势

1. **易于上手**：相对简洁的API和HTML模板使得Vue容易学习和使用。
2. **轻量级**：Vue的核心库较小，对初期加载性能影响较小。
3. **细粒度的响应式系统**：允许更精细地控制数据和视图的更新。

- #### 技术局限性

1. **生态系统规模**：虽然生态系统正在迅速增长，但与React相比仍然较小。
2. **企业接受度**：在全球范围内，特别是西方国家，Vue的企业接受度相对较低。
