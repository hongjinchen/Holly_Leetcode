# REACT

React是一个用于构建用户界面的JavaScript库，特别适用于构建大型、可复用组件的单页应用程序（SPA）。以下是React中一些主要的语法和概念：

### JSX（JavaScript XML）

JSX是一种JavaScript的语法扩展，它允许你**在JavaScript代码中编写类似HTML的标记语言**。它让创建React元素变得更直观。

```jsx
const element = <h1>Hello, world!</h1>;
```

JSX最终会被Babel这样的编译器转换为普通的JavaScript对象。

### 组件（Components）

组件是React应用的基础构建块。它们是独立和可复用的代码块，负责渲染UI的一部分。组件可以是类组件或函数组件。

#### 类组件

类组件使用ES6的类语法定义，并且**可以包含状态（state）和生命周期方法。**

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

**特点**

1. **状态和生命周期**：**类组件允许使用`this.state`来持有局部状态，并通过生命周期方法（如`componentDidMount`，`componentDidUpdate`等）来执行代码。**
2. **this关键字**：在类组件中，**需要使用`this`来访问组件的属性和方法。**
3. **更复杂的UI逻辑**：对于包含复杂交互和状态逻辑的组件，类组件提供了更详细的控制。
4. **继承**：类组件可以继承其他类。

**示例**

```js
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  incrementCount = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={this.incrementCount}>
          Click me
        </button>
      </div>
    );
  }
}
```



#### 函数组件

函数组件是更简单的组件类型，通常用于**不包含状态和生命周期方法**的UI。

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

函数组件是使用**普通JavaScript函数创建的组件**。随着React Hooks的引入，**它们也可以使用状态和其他React特性。**

**特点**

1. **简洁性**：通常**比类组件更简洁，易于阅读和测试**。
2. **Hooks**：**可以通过Hooks（如`useState`，`useEffect`）来使用状态和生命周期特性。**
3. **无this关键字**：不需要使用`this`关键字。
4. **推荐使用**：React团队推荐使用函数组件和Hooks来创建新组件，因为它们更简洁、更易于理解。

**示例**

```js
function MyComponent() {
  const [count, setCount] = useState(0);
  const incrementCount = () => {
    setCount(count + 1);
  };
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={incrementCount}>
        Click me
      </button>
    </div>
  );
}
```



### 状态（State）

状态是一个**组件可以管理的数据，它可以随时间变化，并影响组件的渲染输出**。在类组件中，状态是一个对象，**通过`this.setState`方法更新。**

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }
  render() {
    return (
      <div>
        <p>You clicked {this.state.count} times</p>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Click me
        </button>
      </div>
    );
  }
}
```

在**函数组件**中，可以使用**`useState` Hook**来添加状态。

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### 属性（Props）

**Props是从父组件传递到子组件的只读数据**。它们**在组件内部不应该被修改。**

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
const element = <Welcome name="Sara" />;
```



### 钩子（Hooks）

**Hooks**是React 16.8引入的新特性，它允许你在函数组件中使用状态和其他React特性，如**生命周期**、上下文（context）等。

```jsx
import React, { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  // 相当于类组件中的 componentDidMount 和 componentDidUpdate:
  useEffect(() => {
    document.title = `You clicked ${count} times`;
  });

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

#### 常用的React Hooks

1. **useState**
   - `useState` 用于在函数组件中添加状态。它返回一个状态变量和一个用于更新这个状态的函数。
   - 示例：`const [count, setCount] = useState(0);`

2. **useEffect**
   - `useEffect` 用于处理函数组件中的副作用，类似于类组件中的 `componentDidMount`、`componentDidUpdate` 和 `componentWillUnmount` 生命周期方法的组合。
   - 示例：`useEffect(() => { document.title = `You clicked ${count} times`; });`

3. **useContext**
   - `useContext` 用于让你在函数组件中可以方便地使用React Context API。
   - 示例：`const value = useContext(MyContext);`

4. **useReducer**
   - `useReducer` 用于在组件中引入更复杂的状态逻辑。它通常用于管理组件的多个状态。
   - 示例：`const [state, dispatch] = useReducer(reducer, initialState);`

5. **useCallback**
   - `useCallback` 返回一个记忆化的回调函数，只有当它的依赖发生变化时才会更新。
   - 示例：`const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);`

6. **useMemo**
   - `useMemo` 返回一个记忆化的值，只有当依赖项改变时才会重新计算。
   - 示例：`const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);`

7. **useRef**
   - `useRef` 返回一个可变的ref对象，其`.current`属性被初始化为传入的参数（initialValue）。返回的对象在组件的整个生命周期内保持不变。
   - 示例：`const myRef = useRef(initialValue);`

#### 使用上的限制
1. **只在顶层调用Hooks**：不要在循环、条件或嵌套函数中调用Hooks。这是为了确保Hooks在每次渲染时都以相同的顺序被调用。

2. **只在React函数中调用Hooks**：不要在普通的JavaScript函数中调用Hooks。你可以在React的函数组件或自定义Hook中调用它们。

3. **使用规范**：正确使用依赖数组。例如，在 `useEffect`、`useCallback` 和 `useMemo` 中，你需要正确地指定依赖项数组，以避免不必要的重新渲染或遗漏更新。

4. **避免过度使用useCallback和useMemo**：滥用这些可以创建记忆化值和函数的Hooks可能会导致性能问题，因为它们需要在内存中保存旧的值和函数。

5. **清理副作用**：在使用 `useEffect` 时，如果你的副作用函数返回了一个函数，那么这个返回的函数将在组件卸载时被调用，用于清理副作用。



### 生命周期方法

生命周期方法是**类组件**中的特殊方法，**它们在组件的生命周期的特定时刻被调用，例如组件创建、更新和销毁时。**

```jsx
class MyComponent extends React.Component {
  componentDidMount() {
    // 组件被挂载到DOM后调用
  }

  componentDidUpdate(prevProps, prevState) {
    // 组件更新后调用
  }

  componentWillUnmount() {
    // 组件卸载前调用
  }

  render() {
    return <div>{/* ... */}</div>;
  }
}
```



### 事件处理

React元素可以有事件处理器，它们的命名遵循camelCase约定，而且你需要传递一个函数作为事件处理器，而不是一个字符串。

```jsx
<button
 onClick={activateLasers}>
  Activate Lasers
</button>
```

### 条件渲染

在React中，你可以使用JavaScript运算符来创建表示当前状态的不同UI部分。

```jsx
function Greeting(props) {
  if (props.isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}
```

### 列表与键（Keys）

当你有一个元素数组时，每个元素都应该有一个独一无二的`key`属性，这有助于React识别哪些项被改变、添加或是移除。

```jsx
const todoItems = todos.map((todo) =>
  <li key={todo.id}>
    {todo.text}
  </li>
);
```

### 表单处理

React中的表单元素通常是受控组件，这意味着输入的状态由React的状态控制。

```jsx
class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
```

### 上下文（Context）

Context提供了一种在**组件间共享此类值的方式**，**而不必显式地通过组件树的每个层级传递props**。

```jsx
// 创建一个 Context
const ThemeContext = React.createContext('light');

// 使用Provider来传递当前的theme，任何组件都可以读取它，无论多深
<ThemeContext.Provider value="dark">
  <Toolbar />
</ThemeContext.Provider>

// 在组件中读取Context
function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <Button theme={theme} />;
}
```

### 高阶组件（HOCs）

高阶组件是React中用于重用组件逻辑的高级技术。HOC本身不是React API的一部分，它是一种模式，源自React自身的组合性质。

```jsx
function withSubscription(WrappedComponent, selectData) {
  // 返回另一个组件
  return class extends React.Component {
    constructor(props) {
      super(props);
      this.handleChange = this.handleChange.bind(this);
      this.state = {
        data: selectData(DataSource, props)
      };
    }

    handleChange() {
      this.setState({
        data: selectData(DataSource, this.props)
      });
    }

    // ... 其他生命周期方法 ...

    render() {
      // 使用最新的数据渲染WrappedComponent
      return <WrappedComponent data={this.state.data} {...this.props} />;
    }
  };
}
```

### 状态管理

在更复杂的应用中，状态管理可能会变得复杂，这时候可以使用**Redux**或**Context API**等库来管理应用的状态。

```jsx
import { createStore } from 'redux';

// Redux store的创建
const store = createStore(reducer);

// 在React组件中使用Redux
import { useSelector, useDispatch } from 'react-redux';
function Counter() {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+</button>
      <span>{count}</span>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-</button>
    </div>
  );
}
```



